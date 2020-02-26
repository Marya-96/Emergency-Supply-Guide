from jinja2 import Template

from page_en import Money
from page_en import Water
from page_en import Food
from page_en import Medication
from page_en import GeneralItems
from page_en import Gardening

sections = [Money, Water, Food, Medication, GeneralItems, Gardening]


def convert_content_to_html(string):
  lines = string.split("\n")
  output_string = ""
  for line in lines:
    # Detecting title
    if line[:2] == "# ":
      output_string += "<h4>" + line[2:] + "</h4>"
    # Detecting list
    elif line[:2] == "* ":
      output_string += "<li>" + line[2:] + "</li>"
    # Detecting warning popup
    elif line[:2] == "! ":
      output_string += '<div class="alert alert-warning"><strong>Warning! </strong>' + line[2:] + "</div>"
    else:
      output_string += "<p>" + line + "</p>"
  
  return output_string

# Convert the content part to proper HTML
for section in sections:
  section["content"] = convert_content_to_html(section["content"])

print("Creating the guide...")
template = Template(open('template/t_index.html').read())

f = open("result.html", "w")
f.write(template.render(sections=sections))
f.close()

print("Finished")