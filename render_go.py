#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Copyright (C) 2007 Martin Owens

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex,simplestyle
import sys
import string


WHITE=1
BLACK=0
MARK=2
REMOVE=3

BS=19

def draw_gridline(id, x1,y1,x2,y2,s, parent):

    style = {   'stroke'        :  'black',
                'stroke-width'  :  str(s/16.0 if x1==0 and x2==0 or y1==0 and y2==0 or x1==BS-1 and x2==BS-1 or y1==BS-1 and y2==BS-1 else  s/32.0 ),
                'fill'          : "none"
            }
                
    attribs = {
        'style'     :simplestyle.formatStyle(style),
        'x1'         : str(x1*s+s/2.0 ),
        'y1'         : str((BS-y1-1)*s+s/2.0 ),
        'x2'         : str(x2*s+s/2.0 ),
        'y2'         : str((BS-y2-1)*s+s/2.0 ),
          'id' : id
            }
    circ = inkex.etree.SubElement(parent, inkex.addNS('line','svg'), attribs )

def draw_point(id, x,y,s, parent):

    style = {   'stroke'        :  "none",
                'fill'          : 'black'
            }
    attribs = {
        'style'     :simplestyle.formatStyle(style),
          'cx': str(x*s+s/2.0),
          'cy': str((BS-y-1)*s+s/2.0),
          'r': str(s/12.0),
          'id' : id
            }

    circ = inkex.etree.SubElement(parent, inkex.addNS('circle','svg'), attribs )

def draw_string(x,y,s,n,grp):
    style = {   'font-size': str(s*0.3)+'pt',
                'text-anchor': 'middle',
                'font-family':'Arial',
                'fill'          : "black"
            }
    attribs = {
        'style'     :simplestyle.formatStyle(style),
        'x': str(x),
        'y': str(y), 
          }
    circ=inkex.etree.SubElement(grp,'text',attribs)
    circ.text=unicode(n,'mbcs') if sys.getfilesystemencoding()=='mbcs' else unicode(n,'utf-8')
  
  
def draw_piece(x,y,s,c,n,bc,mono,flip,parent):
  
  if flip:
    x=BS-x-1
  else:
    y=BS-y-1
  
  
  grp_attribs = {'id':'piece'+str(y*100+x)
                    }
  grp = inkex.etree.SubElement(parent, 'g', grp_attribs)

  if c==WHITE:
    style = {   'stroke'        :  "black",
                'stroke-width'  :  str(s/24.0),
                'fill'          : "white"
           }
  elif c==BLACK:
    style = {   'stroke'        :  "black",
                'stroke-width'  :  str(s/24.0),
                'fill'          : "black"
            }
  elif c==MARK:
    style = {   'stroke'        :  "none",
                'stroke-width'  :  str(s/24.0),
                'fill'          : bc
            }
  attribs = {
      'style'     :simplestyle.formatStyle(style),
      'cx': str(x*s+s/2.0),
      'cy': str((y)*s+s/2.0), 
      'r': str(s/2.0*0.9),
        
        }
   
  circ=inkex.etree.SubElement(grp,'circle',attribs)
  
  if isinstance(n,str) and len(n)>0 and n[0]=='!':
    n=n[1:]
    if n=='ma':
      if c==BLACK:
        style = {
          'stroke':'white',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      else:
        style = {
          'stroke':'black',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      attribs = {
          'style'     :simplestyle.formatStyle(style),
          'x1': str(x*s-s*0.25+s/2.0),
          'y1': str(y*s-s*0.25+s/2.0), 
          'x2': str(x*s+s*0.25+s/2.0),
          'y2': str(y*s+s*0.25+s/2.0), 
            
            }
      circ=inkex.etree.SubElement(grp,'line',attribs)
      attribs = {
          'style'     :simplestyle.formatStyle(style),
          'x1': str(x*s-s*0.25+s/2.0),
          'y1': str(y*s+s*0.25+s/2.0), 
          'x2': str(x*s+s*0.25+s/2.0),
          'y2': str(y*s-s*0.25+s/2.0), 
            
            }
      circ=inkex.etree.SubElement(grp,'line',attribs)
    elif n=='tr':
      if c==BLACK:
        style = {
          'stroke':'white',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      else:
        style = {
          'stroke':'black',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      attribs = {
          'style'     :simplestyle.formatStyle(style),
          'points': str(x*s+s/2.0)+','+str(y*s-s*0.4+s/2.0)+' '+
                    str(x*s+s*0.35+s/2.0)+','+str(y*s+s*0.2+s/2.0)+' '+
                    str(x*s-s*0.35+s/2.0)+','+str(y*s+s*0.2+s/2.0)
            
            }
      circ=inkex.etree.SubElement(grp,'polygon',attribs)
    elif n=='sq':
      if c==BLACK:
        style = {
          'stroke':'white',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      else:
        style = {
          'stroke':'black',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      attribs = {
          'style'     :simplestyle.formatStyle(style),
          'x': str(x*s-s*0.28+s/2.0),
          'y': str(y*s-s*0.28+s/2.0),
          'width':str(s*0.56),
          'height':  str(s*0.56)
            }
      circ=inkex.etree.SubElement(grp,'rect',attribs)
    elif n=='cr':
      if c==BLACK:
        style = {
          'stroke':'white',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      else:
        style = {
          'stroke':'black',
          'stroke-width': str(s/16.0),
          'fill':'none'
        }
      attribs = {
          'style'     :simplestyle.formatStyle(style),
          'cx': str(x*s+s/2.0),
          'cy': str(y*s+s/2.0),
          'r':str(s*0.25),
            }
      circ=inkex.etree.SubElement(grp,'circle',attribs)
    else:  
      if c==BLACK:
        style = {   'font-size': str(s*0.4)+'pt',
                    'text-anchor': 'middle',
                    'font-family':'Arial',
                    'fill'          : "white"
                }
      else:
        style = {   'font-size': str(s*0.4)+'pt',
                    'text-anchor': 'middle',
                    'font-family':'Arial',
                    'fill'          : "black"
                }
      attribs = {
          'style'     :simplestyle.formatStyle(style),
          'x': str(x*s+s/2.0),
          'y': str((y)*s+s/2.0+s*0.4/2.0), 
            }
      circ=inkex.etree.SubElement(grp,'text',attribs)
      circ.text=unicode(n,'mbcs') if sys.getfilesystemencoding()=='mbcs' else unicode(n,'utf-8')
  elif not isinstance(n,int) or n>0:
    if c==BLACK:
      style = {   'font-size': str(s*0.4)+'pt',
                  'text-anchor': 'middle',
                  'font-family':'Arial',
                  'fill'          : "white"
              }
    else:
      style = {   'font-size': str(s*0.4)+'pt',
                  'text-anchor': 'middle',
                  'font-family':'Arial',
                  'fill'          : "black"
              }
    attribs = {
        'style'     :simplestyle.formatStyle(style),
        'x': str(x*s+s/2.0),
        'y': str((y)*s+s/2.0+s*0.4/2.0), 
          }
    circ=inkex.etree.SubElement(grp,'text',attribs)
    if isinstance(n,int):
      circ.text=str(n)
    else:
      circ.text=unicode(n,'mbcs') if sys.getfilesystemencoding()=='mbcs' else unicode(n,'utf-8')
      
  
def next(n):
  if isinstance(n,int):
    return n+1
  if isinstance(n,str):
    if len(n)<=0:
      return ''
    if n[0]=='!':
      return n
    if n[-1]>='0' and n[-1]<='8' or n[-1]>='A' and n[-1]<='Y' or n[-1]>='a' and n[-1]<='y':
      n=n[:-1]+chr(ord(n[-1])+1)
      return n
  return n

def fen2board(fen):
  
  b=[[(-1,-1) for i in range(BS)] for j in range(BS) ]
  ws=string.split(fen,' ')
  n=0
  t=BLACK
  for c in ws:
    if len(c)<=0:
      continue
    if c[0]=='#':
      n=c[1:]
      if len(n)>0 and n[0]=='!':
        n='!'+n
      continue
    c=c.lower()
    if c[0]=='!':
      n=c
    if c=='w':
      t=WHITE
    elif c=='b':
      t=BLACK
    elif c=='m':
      t=MARK
    elif c=='r':
      t=REMOVE
    elif c[0]>='a' and c[0]<='z':
      x=ord(c[0])-97 #if c[0]<'i' else 98)
      try:
        y=int(c[1:])-1
      except:
        y=-1
      if x>=0 and x<BS and y>=0 and y<BS:
        if t==REMOVE:
          b[y][x]=(-1,-1)
        else:
          b[y][x]=(t,n)
      n=next(n)
      if t==WHITE:
        t=BLACK
      elif t==BLACK:
        t=WHITE
    elif c[0]>='0' and c[0]<='9':
      n=int(c)
  return b

def render_goboard(fen, piecesize, gc,mono,flip,showcoord, parent):
  piecesize/=2.0
  grp_attribs = {'id':'goboard'
                    }
  grp = inkex.etree.SubElement(parent, 'g', grp_attribs)
  if mono:
    c="white"
  else:
    c="#"+gc

  style = {   'stroke'        :  "none" if mono else "black",
               'stroke-width' : str(piecesize/24.0),
                'fill'          : 'white' if mono else c
            }
  attribs = {
      'style'     :simplestyle.formatStyle(style),
        'x': str(-piecesize/2.0),
        'y': str(-piecesize/2.0),
        'width': str(piecesize*(BS+1)),
        'height': str(piecesize*(BS+1)),
        'id':"board"
        }
  circ=inkex.etree.SubElement(grp,'rect',attribs)

  for y in range(0,BS):
      x1=0
      x2=BS-1
      draw_gridline('lh'+str(y+1),x1,y,x2,y,piecesize,grp)
  for x in range(0,BS):
      y1=0
      y2=BS-1
      draw_gridline('lv'+chr(x+97),x,y1,x,y2,piecesize,grp)
  draw_point('pd4',3,3,piecesize,grp);
  draw_point('pp4',BS-4,3,piecesize,grp);
  draw_point('pd16',3,BS-4,piecesize,grp);
  draw_point('pp16',BS-4,BS-4,piecesize,grp);
  if BS%2!=0:
    draw_point('pk10',BS//2,BS//2,piecesize,grp);
  if showcoord:
    for i in range(BS):
      if flip:
        c1=str(BS-i)
        c2=chr(65+BS-i-1) #if BS-i-1<8 else chr(66+BS-i-1)
      else:
        c1=str(i+1)
        c2=chr(65+i)# if i<8 else chr(66+i)
      draw_string(-piecesize/4.0,(BS-i)*piecesize-piecesize/3.0,piecesize,c1,grp)
      draw_string((BS)*piecesize+piecesize/5.0,(BS-i)*piecesize-piecesize/3.0,piecesize,c1,grp)
      draw_string((i+1)*piecesize-piecesize/2.0,BS*piecesize+piecesize/3.0,piecesize,c2,grp)
      draw_string((i+1)*piecesize-piecesize/2.0,-piecesize/16.0,piecesize,c2,grp)


  grp_attribs = {'id':'pieces'
                    }
  grp = inkex.etree.SubElement(parent, 'g', grp_attribs)
  b=fen2board(fen)
  for y in range(0,BS):
    for x in range(0,BS):
      (p,t)=b[y][x]
      if p!=-1 and t!=-1:
        draw_piece(x,y,piecesize,p,t,c,mono,flip,grp)

class InsertGoBoard(inkex.Effect):
   

  def __init__(self):
    inkex.Effect.__init__(self)
    self.OptionParser.add_option("-p", "--piecesize",
            action="store", type="int",
            dest="piecesize", default=16,
            help="Piece size")
    self.OptionParser.add_option("-b", "--boardsize",
            action="store", type="int",
            dest="boardsize", default=19,
            help="Board size")
    self.OptionParser.add_option("-k", "--kifu",
            action="store", type="string",
            dest="kifu", default="w d4 1 f3 g3 #A c6 e6 !MA e7 d7 !TR e9 d9 !CR e10 d8 !SQ d10 d5 0 d11 m #A d12 d13",
            help="KIFU")
            
    self.OptionParser.add_option("-c", "--boardcolor",
            action="store", type="string",
            dest="boardcolor", default="c08000",
            help="Color of board")
    self.OptionParser.add_option("-m", "--mono",
            action="store", type="inkbool",
            dest="mono", default=True,
            help="monochrome")
    self.OptionParser.add_option("-s", "--showcoord",
            action="store", type="inkbool",
            dest="showcoord", default=False,
            help="show coordinate")
    self.OptionParser.add_option("-r", "--flip",
            action="store", type="inkbool",
            dest="flip", default=True,
            help="flipboard")
           


  def effect(self):
    so = self.options
    x, y = self.view_center
    size=so.piecesize*self.unittouu('1mm')
    global BS
    BS=so.boardsize
    x-=size*BS/4.0
    y-=size*BS/4.0
    grp_transform = 'translate' + str( (x,y) )
    grp_name = 'GoBoard'
    grp_attribs = { inkex.addNS('label','inkscape'):grp_name,
                   'transform':grp_transform }
    grp = inkex.etree.SubElement(self.current_layer, 'g', grp_attribs)#the group to put everything in

    render_goboard(so.kifu, size, so.boardcolor, so.mono, so.flip, so.showcoord, grp )    # generate the SVG elements

if __name__ == '__main__':
        e = InsertGoBoard()
        e.affect()

