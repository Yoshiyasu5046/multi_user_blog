#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates2")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# form_html = """
# <form>
# <h2>Add a Food</h2>
# <input type="text" name="food">
# <button>Add</button>
# </form>
# """

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		self.render("shopping_list.html")

		# output = form_html
		# output_hidden = ""
		
		# items = self.request.get_all("food")
		# output_items = ""
		# if items:
		# 	for item in items:
		# 		output_hidden += hidden_html % item
		# 		output_items += item_html % item

		# 	output_shopping = shopping_list_html % output_items
		# 	output += output_shopping

		# 	self.write(output)


app = webapp2.WSGIApplication([
	('/', MainPage)
], debug=True)



