* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-extractAO.html

#  [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html).extractAO
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html "Go to LightingSettings Component in the Manual")
extractAO; 
### Description
Whether the Progressive Lightmapper extracts Ambient Occlusion to a separate lightmap. (Editor only).
When this is set to `true`, Unity saves the filtered Ambient Occlusion (AO) texture to disk as a separate lightmap, in addition to applying it to the regular lightmaps. When this is set to `false`, Unity does not save the filtered AO texture to disk separately.  
  
Use this if you need to access the AO data separately.  
  
Note that the values from [aoExponentDirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-aoExponentDirect.html) and [aoExponentIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-aoExponentIndirect.html) are not applied; instead, the default values are used. The resulting lightmap is saved to disk in the same location as the other lightmaps.  
  
This only works when [autoGenerate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-autoGenerate.html) is set to `false`, and [ao](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-ao.html) is set to `true`.  
  
Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html), [trainingDataDestination](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-trainingDataDestination.html).
* * *
