* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState-ctor.html

# RasterState Constructor
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
## Declaration
public RasterState([Rendering.CullMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullMode.html) cullingMode, int offsetUnits, float offsetFactor, bool depthClip); 
### Parameters
Parameter | Description  
---|---  
cullingMode | Controls which sides of polygons should be culled (not drawn).  
offsetUnits | Scales the minimum resolvable depth buffer value in the GPU's depth bias setting.  
offsetFactor | Scales the maximum Z slope in the GPU's depth bias setting.  
### Description
Creates a new raster state with the given values.
* * *
