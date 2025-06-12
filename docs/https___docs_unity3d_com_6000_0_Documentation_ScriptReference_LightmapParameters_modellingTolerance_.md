* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-modellingTolerance.html

#  [LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html).modellingTolerance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html "Go to LightmapParameters Component in the Manual")
modellingTolerance; 
### Description
Maximum size of gaps that can be ignored for GI (multiplier on pixel size).
Can be used to alleviate issues when objects are close together and the gap between the objects should not be used in the calculation of GI. In some cases having an object near a surface may cause a dark halo on the surface around the perimeter of the object because there is a small gap between the object and the surface where nearly no light will enter causing a very dark pixel. These dark pixels can look bad if they are partially visible and not completely obscured by the object. Increasing the modelling tolerance will make the GI calculation ignore the parts of the pixel that are very near another surface. The value is multiplier on the pixel size. If you want to ignore 5cm gaps with a real-time resolution of 2 texels per meter you would need a modelling tolerance of 0.01.
* * *
