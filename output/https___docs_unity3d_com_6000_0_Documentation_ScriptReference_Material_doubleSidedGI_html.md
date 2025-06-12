* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-doubleSidedGI.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).doubleSidedGI
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
doubleSidedGI; 
### Description
Gets and sets whether the Double Sided Global Illumination setting is enabled for this material.
When enabled, the lightmapper accounts for both sides of the geometry when calculating Global Illumination. Backfaces are not rendered or added to lightmaps, but get treated as valid when seen from other objects. When using the Progressive Lightmapper backfaces bounce light using the same emission and albedo as frontfaces. (Currently this setting is only available when baking with the Progressive Lightmapper backend.)
* * *
