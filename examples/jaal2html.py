# Reads wrapped JAAL 2.0 data downloaded directly from A+.
# Produces a HTML file describing the data in a human-readable format.

import base64
import html
import json
import zlib
from pathlib import Path

class SemanticExplainer:
    """
    Explains semantic JAAL data as preformatted text.
    """

    def __init__(self):
        # Entire JAAL data
        self.jaal = []

        # dict: from JAAL id (str) to human-readable name (str)
        self.id_to_name = dict()

        # dict: from JAAL id (str) to corresponding objtct
        self.id_to_obj = dict()

    def set_jaal(self, jaal):
        self.jaal = jaal
        self.id_to_obj = dict()
        self.id_to_name = dict()

    def analyse_data_structure(self, ds):
        """
        Analyzes a data structure to be able to describe it.

        Returns: multiline string
        """        
        if 'dsClass' not in ds:
            return "Unknown data (no dsClass):\n{}\n".format(
                json.dumps(obj=ds, indent=4))

        if ds['dsClass'] == 'graph':
            return self.analyse_graph(ds)
        
        return "Unknown data structure: dsClass = {}\n{}\n".format(
            ds['dsClass'], json.dumps(obj=ds, indent=4))
            

    def analyse_graph(self, g):
        """
        Produces preformatted text about a semantic data of a JAAL graph to the
        HTML file.

        Returns: multiline string
        """
        
        self.id_to_obj[g['id']] = g
        self.id_to_name[g['id']] = g['id']
        output = []
        w = output.append
        required_keys = set(['id', 'dsClass', 'edge', 'node', 'directed'])
        w("Graph:\n")
        w(f"  id: {g['id']}\n")        
        w(f"  directed: {g['directed']}\n")
        w(f"  nodes:\n")
        w(self.generate_node_descriptions(g['node']))
        w(f"  edges:\n")
        w(self.generate_edge_descriptions(g['edge']))
        for key, value in g.items():
            if key not in required_keys:
                json_text = json.dumps(obj=value, indent=4)
                w(f"  {key}: {json_text}\n")
        return "".join(output)
    
    def generate_node_descriptions(self, nodes):
        """
        Generates descriptions of a list of JAAL nodes.

        Parameters:
        nodes (list): list of objects, where each objects has at least the
                      following keys: key, id.

        Returns: multiline string
        """
        output = []
        for node in nodes:
            self.id_to_name[node['id']] = f"node {node['key']}"
            self.id_to_obj[node['id']] = node
            node_str = self.node_to_str(node);
            output.append(f"    {node_str}\n")
        return "".join(output)
    
    def node_to_str(self, node):
        """
        Generates a one-line string representation of a JAAL node.

        Returns: multiline string
        """
        output = [f"{node['id']} :"]
        for key, value in node.items():
            if key != 'id':
                output.append(f" {key}: {value},")
        return "".join(output)[0:-1] # trim the last comma

    def generate_edge_descriptions(self, edges):
        """
        Generates descriptions of a list of JAAL edges.

        Parameters:
        edges (list): list of objects, where each objects has at least the
                      following keys: key, id.

        Returns: multiline string
        """
        output = []
        for edge in edges:        
            v1_label = self.id_to_obj[edge['node'][0]]['key']
            v2_label = self.id_to_obj[edge['node'][1]]['key']
            if v2_label < v1_label:
                v1_label, v2_label = v2_label, v1_label
            self.id_to_name[edge['id']] = f"edge {v1_label}{v2_label}"
            output.append(f"    {self.edge_to_str(edge)}\n")
        return "".join(output)

    def edge_to_str(self, edge):
        """
        Generates a one-line string representation of a JAAL edge.

        Returns: multiline string
        """
        if edge['id'] not in self.id_to_name:
            raise Exception(
                f"Set self.id_to_name for {edge['id']} before calling me!")
        
        output = [f"{self.id_to_name[edge['id']]} :"]
        w = output.append
        
        for key, value in edge.items():
            if key not in ['id', 'node']:
                json_text = json.dumps(obj=value, indent=4)
                w(f" {key}: {json_text},")
        return "".join(output)[0:-1] # trim the last comma
    
    def analyse_animation_step(self, step):
        """
        Analyses a JAAL animation step.

        Returns: multiline string
        """

        if 'type' not in step:
            return "Invalid animation step: no 'type' field!"
        
        output = []
        w = output.append
        
        w(f"type: {step['type']}\n")
        w(f"time: {step['time'] * 0.001} s\n")
        if step['type'] == "click":
            w(self.__analyse_click_step(step))
        if step['type'] == "undo":
            pass
        if step['type'] == "grade":
            pass        
        return "".join(output)

    def __analyse_click_step(self, step):
        """
        Analyses a JAAL animation step type 'click'.
        Returns: multiline string
        """
        output = []
        w = output.append
        w(f"gradable: {step['gradable']}\n")
        w( "object  : {}\n".format(self.id_to_name[step['object']]))
        for key, value in step.items():
            if key not in ['type', 'time', 'gradable', 'object', 'image']:
                json_text = self.__explain_custom_data(key, value)
                w(f"{key}: {json_text}\n")                
        return "".join(output)[0:-1] # trim the last comma
    
    def __explain_custom_data(self, key, value):
        """
        Attempts to explain custom data in click steps, e.g.
        keys `pqIn` and `pqOut` produced by Scaffolded Prim & Dijkstra
        exercises.
        """

        # If the value is a string, sniff whether it is a JAAL id
        if str(type(value)) == "<class 'str'>":
            if value in self.id_to_name:
                return self.id_to_name[value]
        return json.dumps(obj=value, indent=4)


    
    def analyse_model_step(self, step):
        """
        Analyses a JAAL model answer step.

        Returns: multiline string
        """

        if 'type' not in step:
            return "Invalid model answer step: no 'type' field!"

        return json.dumps(obj=step, indent=4)
    


class JaalDecoder:
    """
    Decodes JAAL data and converts it to HTML.
    """
    
    def __init__(self):
        self.jaal = None
        self.htmlfile = None
        self.explainer = SemanticExplainer()

    def read_json_file(self, filepath):        
        """
        Reads a JSON file downloaded from A+ LMS. Unwraps it if necessary.

        Parameters:
        filepath (pathlib.Path): a Path to the JSON file
        """    
        f = open(file)
        self.jaal = json.load(f)
        f.close()

        if (self.jaal_is_aplus_wrapped()):
            self.jaal = self.decode_wrapped()

        self.explainer.set_jaal(self.jaal)

    def jaal_is_aplus_wrapped(self):
        """
        Detects whether the data is 'A+ wrapped', meaning that JSAV Exercise
        Recorder has wrapped the actual JAAL data into another layer of JSON.

        Returns: either True or False
        """

        # The wrapping looks like this:
        # {
        #   "description": "JAAL 2.0 recording",
        #   "generator": "JSAV Exercise Recorder 2.0.1",
        #   "encoding":
        #     "JSON string -> HTML escape -> zlib compress -> Base64 encode",
        #   "data": ...
        # }
        return 'description' in self.jaal and \
            self.jaal['description'] == "JAAL 2.0 recording"

    def decode_wrapped(self):
        """
        Decodes 'A+ wrapped' data
        """
        
        jaal_data = bytes(self.jaal['data'], encoding='ascii')
        decoded = base64.decodebytes(jaal_data)
        unzipped = zlib.decompress(decoded)
        unzipped_str = str(unzipped)
        unzipped_str = unzipped_str[2:-1]
        unescaped = html.unescape(unzipped_str)
        unescaped = unescaped.replace(r'\\"', r'\"')
        unescaped = unescaped.replace(r'\\n', r'\n')
        unescaped = str(unescaped)
        return json.loads(unescaped)    

    def print_metadata(self):
        print(json.dumps(self.jaal['metadata']), indent=4)

    def open_html_file(self, filepath):
        self.htmlfile = open(filepath, 'w')

    def close_html_file(self):
        self.htmlfile.close()

    def write_header(self, submission_id):
        self.htmlfile.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>JAAL subm. {submission_id}</title>
<meta charset="UTF-8">""")
        
        self.htmlfile.write("""
<style type="text/css">
table {
    border-collapse: collapse;
}
td {
    border: 1px solid black;
    vertical-align: top;
}
code.jsonpath {
    background: #8dffef;
}
</style>
</head>
<body>
""")
        self.htmlfile.write('<h1>Submission {0}</h1>\n'.format(submission_id))

    def write_footer(self):
        self.htmlfile.write('</body>\n')
        self.htmlfile.write('</html>\n')

    def write_metadata(self):
        w = self.htmlfile.write
        w('<h2>Metadata</h2>\n')
        self.write_jaal_path('metadata')
        self.htmlfile.write('<pre>')
        json.dump(obj=self.jaal['metadata'], fp=self.htmlfile, indent=4)
        self.htmlfile.write('</pre>\n')

    def write_jaal_path(self, path):
        """
        Generates a <p> element describing a JSON path starting with a '$'.        

        Parameters:
        path (str): a JSON path
        """
        self.htmlfile.write(
            f'<p>JSON path: <code class="jsonpath">$.{path}</code></p>\n')

    def write_definitions(self):
        w = self.htmlfile.write
        w('<h2>Definitions</h2>\n')
        self.write_jaal_path('definitions')
        w('<pre>')
        for key, value in self.jaal['definitions'].items():
            if key == 'modelAnswer':
                w('modelAnswer: <a href="#modelanswer">see it here</a>\n')
            else:
                w("{}: {}\n".format(key, json.dumps(obj=value, indent=4)))
        w('</pre>')


    def write_initial_state(self):
        """
        Writes data about the initial state of the exercise.
        """
        w = self.htmlfile.write
        w('<h2>Initial state</h2>\n')
        self.write_jaal_path('initialState')
        w("""
<table>
<tr><th>Semantics</th><th>Graphics</th></tr>\n""")
        w("<tr><td>")
        self.write_jaal_path('initialState.dataStructures')
        w("<pre>\n")
        
        for ds in self.jaal['initialState']['dataStructures']:
            w(self.explainer.analyse_data_structure(ds))
            w("\n")
        w("</pre></td>\n")
        studentSvg = self.jaal['initialState']['svg']
        w("<td>")
        self.write_jaal_path('initialState.svg')
        w(f"{studentSvg}</td></tr>")
        w("</table>\n")

    def write_student_solution(self):
        w = self.htmlfile.write
        w("""
<h2>Student's solution</h2>
<table>
<tr><th>Step</th><th>Semantics</th><th>Graphics</th></tr>\n""")
        
        for i in range(len(self.jaal['animation'])):
            step = self.jaal['animation'][i]
            semantics = self.explainer.analyse_animation_step(step)          
            graphics = step['image'] if 'image' in step else ""
            w(f"<tr><td>{i + 1}</td><td>")
            self.write_jaal_path(f"animation[{i}]")            
            w(f"<pre>{semantics}</pre></td><td>")
            self.write_jaal_path(f"animation[{i}].image")
            w(f"{graphics}</td><tr>\n")

        w("</table>\n")

    def write_model_answer(self):
        """
        Produces a HTML table of model answer steps.
        """
        w = self.htmlfile.write
        w("""
<a name="modelanswer">
<h2>Model answer</h2>
</a>
<table>
<tr><th>Step</th><th>Semantics</th><th>Graphics</th></tr>\n""")
        
        modelAnswer = self.jaal['definitions']['modelAnswer']
        for i in range(len(modelAnswer)):
            step = modelAnswer[i]
            # Steps may have substeps
            if str(type(step)) == "<class 'list'>":
                for j in range(len(step)):                    
                    stepno = f"{i+1}.{j+1}"
                    jaalpath = f"definitions.modelAnswer[{i}][{j}]"
                    self.__write__model_answer_step(step[j], stepno, jaalpath)
            else:
                stepno = i + 1
                jaalpath = f"definitions.modelAnswer[{i}]"
                self.__write__model_answer_step(step[j], stepno, jaalpath)
        w("</table>\n")   

    def __write__model_answer_step(self, step, stepno, jaalpath):
        """
        Produces a HTML table row of a model answer step.

        Parameters:
        step (obj): a model answer step
        stepno (str): step number
        jaalpath (str): JAAL JSON path of the step
        """
        w = self.htmlfile.write
        semantics = self.explainer.analyse_model_step(step)
        graphics = step['svg'] if 'svg' in step else ""       

        w(f"<tr><td>{stepno}</td><td>")
        self.write_jaal_path(jaalpath)            
        w(f"<pre>{semantics}</pre></td><td>")
        self.write_jaal_path(f"{jaalpath}.image")
        w(f"{graphics}</td><tr>\n")


###################################################
# Main program
###################################################

p = Path(".")
# In case the script is not run from its directory, but the project root
# 'dijkstra-misconceptions', change it to the correct directory.
# This might happen with VS code debugger.
if (p.cwd().name == "dijkstra-misconceptions"):
    p = Path("data/2023/test")
files = p.glob("*.json")

decoder = JaalDecoder()

for file in files:

    print("Reading {}".format(file))
    decoder.read_json_file(file)

    submission_id = file.name[0:-5]
    decoder.open_html_file(p / 'html' / (submission_id + '.html'))
    decoder.write_header(submission_id)    
    decoder.write_metadata()
    decoder.write_definitions()
    decoder.write_initial_state()
    decoder.write_student_solution()
    decoder.write_model_answer()
    decoder.write_footer()
    decoder.close_html_file()    


