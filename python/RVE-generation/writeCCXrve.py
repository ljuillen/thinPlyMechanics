# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def writeCCXrve(spaceDim=None,workDir=None,project=None,*args,**kwargs):
    varargin = writeCCXrve.varargin
    nargin = writeCCXrve.nargin

    ##
#==============================================================================
# Copyright (c) 2016 Universit de Lorraine & Lule tekniska universitet
# Author: Luca Di Stasio <luca.distasio@gmail.com>
#                        <luca.distasio@ingpec.eu>
    
    # Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 
# Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the distribution
# Neither the name of the Universit de Lorraine or Lule tekniska universitet
# nor the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#==============================================================================
    
    #  DESCRIPTION
#  
#  A function to generate FEM models of RVEs with CALCULIX, here space
#  dimension selection takes place
    
    #  Output:
    
    ##
    
    if 1 == spaceDim:
        writeCCXrve2D(workDir,project)
    else:
        if 2.5 == spaceDim:
            writeCCXrve2andHalfD(workDir,project)
        else:
            if 3 == spaceDim:
                writeCCXrve3D(workDir,project)
            else:
                writeCCXrve2D(workDir,project)
    
    return