# Copyright (c) 2010-2011, Gabriele Favalessa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re, markdown

import asciimathml

class ASCIIMathMLExtension(markdown.Extension):
    def __init__(self, configs):
        pass

    def extendMarkdown(self, md, md_globals):
        self.md = md

        RE = re.compile(r'^(.*)\$\$([^\$]*)\$\$(.*)$', re.M) # $$ a $$

        md.inlinePatterns.add('', ASCIIMathMLPattern(RE), '_begin')

    def reset(self):
        pass

class ASCIIMathMLPattern(markdown.inlinepatterns.Pattern):
    def getCompiledRegExp(self):
        return re.compile(r'^(.*)\$\$([^\$]*)\$\$(.*)$', re.M) # $$ a $$

    def handleMatch(self, m):
        if markdown.version_info < (2, 1, 0):
            math = asciimathml.parse(m.group(2).strip(), markdown.etree.Element,
                       markdown.AtomicString)
        else:
            math = asciimathml.parse(m.group(2).strip(),
                       markdown.util.etree.Element, markdown.util.AtomicString)
        math.set('xmlns', 'http://www.w3.org/1998/Math/MathML')
        return math

def makeExtension(configs=None):
    return ASCIIMathMLExtension(configs=configs)
