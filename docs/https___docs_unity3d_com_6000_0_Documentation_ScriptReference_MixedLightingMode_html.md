* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MixedLightingMode.html

# MixedLightingMode
enumeration
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Enum describing what lighting mode to be used with Mixed lights.
Summary of the baked data associated with each mode:  
  
**IndirectOnly**   
Lightmaps 
  * direct: no
  * occlusion: no


Light probes 
  * direct: no
  * occlusion: no


**Shadowmask**   
Lightmaps 
  * direct: no
  * occlusion: yes


Light probes 
  * direct: no
  * occlusion: yes


**Subtractive**   
Light maps 
  * direct: yes
  * occlusion: no


Light probes 
  * direct: no
  * occlusion: yes


### Properties
Property | Description  
---|---  
[IndirectOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MixedLightingMode.IndirectOnly.html) | Mixed lights provide real-time direct lighting while indirect light is baked into lightmaps and light probes.  
[Shadowmask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MixedLightingMode.Shadowmask.html) | Mixed lights provide real-time direct lighting. Indirect lighting gets baked into lightmaps and light probes. Shadowmasks and light probe occlusion get generated for baked shadows. The Shadowmask Mode used at run time can be set in the Quality Settings panel.  
[Subtractive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MixedLightingMode.Subtractive.html) | Mixed lights provide baked direct and indirect lighting for static objects. Dynamic objects receive real-time direct lighting and cast shadows on static objects using the main directional light in the Scene.  
* * *
