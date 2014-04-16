"""Chemistry renderer module."""

#TODO ADD
#import template_file_for_html

#TODO = REMOVE  SRC PART !!!!


from mfr import config as core_config
def render_chemistry_tag(fp, src=None, alt=''):
    """A simple chemistry file tag renderer.

    fp : full file path

    :param str:
    """

    out =  """
       <div id="uploaded_file" style="width: 1200px; height: 900px; background-color: black;">
       </div> <textarea id="uploaded_file_src" style="display: none;"> \n"""
    input_file = open(fp, "r")
    text_file = input_file.read()
    input_file.close()

    out += text_file
    out_end = """
                </textarea>
                <script src="{static_url}/js/jquery-1.7.min.js"></script>
                <script src="{static_url}/js/Three49custom.js"></script>
                <script type="{static_url}/text/javascript" src="js/GLmol.js"></script>
                <script type="{static_url}/text/javascript">
                var uploaded_file = new GLmol('uploaded_file');
                </script>\n""".format(static_url=core_config['STATIC_URL'])
    return out + out_end