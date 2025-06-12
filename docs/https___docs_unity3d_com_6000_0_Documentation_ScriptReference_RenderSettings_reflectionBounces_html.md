* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-reflectionBounces.html

#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html).reflectionBounces
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
reflectionBounces; 
### Description
The number of times a reflection includes other reflections.
Defines in how many passes reflections are calculated. In a given pass, the Scene is rendered into a cubemap with the reflections calculated in the previous pass applied to reflective objects.  
  
If set to 1, the Scene will be rendered once, which means that a reflection will not be able to reflect another reflection and reflective objects will show up black, when seen in other reflective surfaces.  
  
If set to 2, the Scene will be rendered twice and reflective objects will show reflections from the first pass, when seen in other reflective surfaces.
* * *
