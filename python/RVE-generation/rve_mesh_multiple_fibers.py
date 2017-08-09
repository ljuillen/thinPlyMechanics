# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def rve_mesh(fiberArrangement=None,isUpperBounded=None,isLowerBounded=None,isCohesive=None,crackType=None,element=None,order=None,optimize=None,Rf=None,Vff=None,tratio=None,theta=None,deltatheta=None,f1=None,f2=None,f3=None,N1=None,N2=None,N3=None,N4=None,N5=None,N6=None,*args,**kwargs):
    varargin = rve_mesh.varargin
    nargin = rve_mesh.nargin

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
#  A function to perform
    
    #  Input: isBounded = true; # flag for model type
# 
# Rf = 1; #[10^-6 m] Fiber diameter in micrometers. 
#         # Carbon fibers have a tipical diameter between 5 and 10 
#         # micrometers, glass fibers between 3 and 20
# Vff = 0.6; #[-] Fiber volume fraction
# tratio = 0.6; # [-] ratio of [0] ply thickness to [90] ply thickness
# theta = 30; #[] angular position of crack
# theta = theta*pi/180;
# deltatheta = 10; #[] angular aperture of crack
# deltatheta = deltatheta*pi/180;
# 
# f1 = 0.5; #[-] Innermost square mesh region side defined by 2*f1*Rf
# f2 = 0.77; #[-] Inner circular mesh region radius defined by f2*Rf
# f3 = 1.05; #[-] Outer circular mesh region radius defined by f2*Rf
# 
# #Number of elements:
# N1 = 20; #[-] Notice that angular resolution is equal to 90/N1
# N2 = 10; #[-] 
# N3 = 8; #[-] 
# N4 = 5; #[-] 
# N5 = 20; #[-] 
# N6 = 20; #[-] 
#  Output:
    
    ##
    
    if 1 == fiberArrangement:
        if 1 == crackType:
            if element == 1:
                if order == 1:
                    nodes,edges,elements,fiberN,matrixN,part6bot,part6up,fiberEl,matrixEl,cohesiveEl,boundedBot,boundedUp,gammaNo1,gammaNo2,gammaNo3,gammaNo4,gammaEl1,gammaEl2,gammaEl3,gammaEl4,NintUpNine,NintUpZero,NintBotNine,NintBotZero,NintUpNineCorners,NintUpZeroCorners,NintBotNineCorners,NintBotZeroCorners,NbotRight,NbotLeft,NupRight,NupLeft,EintUpNine,EintUpZero,EintBotNine,EintBotZero,EbotRight,EbotLeft,EupRight,EupLeft,Ncorners,Ndown,Nright,Nup,Nleft,Edown,Eright,Eup,Eleft=rve_mesh_F1_C1_quad1(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=49)
                else:
                    if order == 2:
                        nodes,edges,elements=rve_mesh_F1_C1_quad2(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=3)
            else:
                if order == 1:
                    nodes,edges,elements,fiberN,matrixN,part6bot,part6up,fiberEl,matrixEl,cohesiveEl,boundedBot,boundedUp,gammaNo1,gammaNo2,gammaNo3,gammaNo4,gammaEl1,gammaEl2,gammaEl3,gammaEl4,NintUpNine,NintUpZero,NintBotNine,NintBotZero,NintUpNineCorners,NintUpZeroCorners,NintBotNineCorners,NintBotZeroCorners,NbotRight,NbotLeft,NupRight,NupLeft,EintUpNine,EintUpZero,EintBotNine,EintBotZero,EbotRight,EbotLeft,EupRight,EupLeft,Ncorners,Ndown,Nright,Nup,Nleft,Edown,Eright,Eup,Eleft=rve_mesh_F1_C1_tri1(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=49)
                    if optimize:
                        boundary=matlabarray(cat([Ncorners],[Ndown],[Nright],[Nup],[Nleft],[NbotRight],[NbotLeft],[NupRight],[NupLeft],[gammaNo1],[gammaNo2],[gammaNo3],[gammaNo4,NintUpNine],[NintUpZero],[NintBotNine],[NintBotZero],[NintUpNineCorners],[NintUpZeroCorners],[NintBotNineCorners],[NintBotZeroCorners]))
                        obj=0.9
                        tol=0.01
                        maxIt=100
                        nodes,edges,elements=tri3optimize(nodes,edges,elements,boundary,obj,tol,maxIt,nargout=3)
                else:
                    if order == 2:
                        nodes,edges,elements=rve_mesh_F1_C1_tri2(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=3)
        else:
            if 2 == crackType:
                if element == 1:
                    if order == 1:
                        nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C2_quad1(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
                    else:
                        if order == 2:
                            nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C2_quad2(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
                else:
                    if order == 1:
                        nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C2_tri1(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
                    else:
                        if order == 2:
                            nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C2_tri2(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
            else:
                if 3 == crackType:
                    if element == 1:
                        if order == 1:
                            nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C3_quad1(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
                        else:
                            if order == 2:
                                nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C3_quad2(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
                    else:
                        if order == 1:
                            nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C3_tri1(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
                        else:
                            if order == 2:
                                nodes,edges,elements,gammaNo1,gammaNo2,gammaEl1,gammaEl2=rve_mesh_F1_C3_tri2(isUpperBounded,isLowerBounded,isCohesive,Rf,Vff,tratio,theta,deltatheta,f1,f2,f3,N1,N2,N3,N4,N5,N6,nargout=7)
    else:
        if 2 == fiberArrangement:
            pass
        else:
            if 3 == fiberArrangement:
                pass
            else:
                if 4 == fiberArrangement:
                    pass
                else:
                    if 5 == fiberArrangement:
                        pass
                    else:
                        if 6 == fiberArrangement:
                            pass
                        else:
                            if 7 == fiberArrangement:
                                pass
    
    if logical_not(exist('nodes')):
        nodes=matlabarray([])
    
    if logical_not(exist('edges')):
        edges=matlabarray([])
    
    if logical_not(exist('elements')):
        elements=matlabarray([])
    
    if logical_not(exist('fiberN')):
        fiberN=matlabarray([])
    
    if logical_not(exist('matrixN')):
        matrixN=matlabarray([])
    
    if logical_not(exist('part6bot')):
        part6bot=matlabarray([])
    
    if logical_not(exist('part6up')):
        part6up=matlabarray([])
    
    if logical_not(exist('fiberEl')):
        fiberEl=matlabarray([])
    
    if logical_not(exist('matrixEl')):
        matrixEl=matlabarray([])
    
    if logical_not(exist('cohesiveEl')):
        cohesiveEl=matlabarray([])
    
    if logical_not(exist('boundedBot')):
        boundedBot=matlabarray([])
    
    if logical_not(exist('boundedUp')):
        boundedUp=matlabarray([])
    
    if logical_not(exist('gammaNo1')):
        gammaNo1=matlabarray([])
    
    if logical_not(exist('gammaNo2')):
        gammaNo2=matlabarray([])
    
    if logical_not(exist('gammaNo3')):
        gammaNo3=matlabarray([])
    
    if logical_not(exist('gammaNo4')):
        gammaNo4=matlabarray([])
    
    if logical_not(exist('gammaEl1')):
        gammaEl1=matlabarray([])
    
    if logical_not(exist('gammaEl2')):
        gammaEl2=matlabarray([])
    
    if logical_not(exist('gammaEl3')):
        gammaEl3=matlabarray([])
    
    if logical_not(exist('gammaEl4')):
        gammaEl4=matlabarray([])
    
    if logical_not(exist('NintUpNine')):
        NintUpNine=matlabarray([])
    
    if logical_not(exist('NintUpZero')):
        NintUpZero=matlabarray([])
    
    if logical_not(exist('NintBotNine')):
        NintBotNine=matlabarray([])
    
    if logical_not(exist('NintBotZero')):
        NintBotZero=matlabarray([])
    
    if logical_not(exist('NintUpNineCorners')):
        NintUpNineCorners=matlabarray([])
    
    if logical_not(exist('NintUpZeroCorners')):
        NintUpZeroCorners=matlabarray([])
    
    if logical_not(exist('NintBotNineCorners')):
        NintBotNineCorners=matlabarray([])
    
    if logical_not(exist('NintBotZeroCorners')):
        NintBotZeroCorners=matlabarray([])
    
    if logical_not(exist('NbotRight')):
        NbotRight=matlabarray([])
    
    if logical_not(exist('NbotLeft')):
        NbotLeft=matlabarray([])
    
    if logical_not(exist('NupRight')):
        NupRight=matlabarray([])
    
    if logical_not(exist('NupLeft')):
        NupLeft=matlabarray([])
    
    if logical_not(exist('EintUpNine')):
        EintUpNine=matlabarray([])
    
    if logical_not(exist('EintUpZero')):
        EintUpZero=matlabarray([])
    
    if logical_not(exist('EintBotNine')):
        EintBotNine=matlabarray([])
    
    if logical_not(exist('EintBotZero')):
        EintBotZero=matlabarray([])
    
    if logical_not(exist('EbotRight')):
        EbotRight=matlabarray([])
    
    if logical_not(exist('EbotLeft')):
        EbotLeft=matlabarray([])
    
    if logical_not(exist('EupRight')):
        EupRight=matlabarray([])
    
    if logical_not(exist('EupLeft')):
        EupLeft=matlabarray([])
    
    if logical_not(exist('Ncorners')):
        Ncorners=matlabarray([])
    
    if logical_not(exist('Ndown')):
        Ndown=matlabarray([])
    
    if logical_not(exist('Nright')):
        Nright=matlabarray([])
    
    if logical_not(exist('Nup')):
        Nup=matlabarray([])
    
    if logical_not(exist('Nleft')):
        Nleft=matlabarray([])
    
    if logical_not(exist('Edown')):
        Edown=matlabarray([])
    
    if logical_not(exist('Eright')):
        Eright=matlabarray([])
    
    if logical_not(exist('Eup')):
        Eup=matlabarray([])
    
    if logical_not(exist('Eleft')):
        Eleft=matlabarray([])
    
    return nodes,edges,elements,fiberN,matrixN,part6bot,part6up,fiberEl,matrixEl,cohesiveEl,boundedBot,boundedUp,gammaNo1,gammaNo2,gammaNo3,gammaNo4,gammaEl1,gammaEl2,gammaEl3,gammaEl4,NintUpNine,NintUpZero,NintBotNine,NintBotZero,NintUpNineCorners,NintUpZeroCorners,NintBotNineCorners,NintBotZeroCorners,NbotRight,NbotLeft,NupRight,NupLeft,EintUpNine,EintUpZero,EintBotNine,EintBotZero,EbotRight,EbotLeft,EupRight,EupLeft,Ncorners,Ndown,Nright,Nup,Nleft,Edown,Eright,Eup,Eleft