* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Clear.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).Clear
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
public static void Clear(); 
### Description
Deletes all runtime data for the currently loaded Scenes.
This method deletes the following: baked and real-time lightmaps, Enlighten Realtime Global Illumination metadata, baked output on Lights, and baked and real-time data on instances (index, ST and per-instance UVs).  
  
This method does not delete lightmaps, Reflection Probes, or the Lighting Data Asset. See also: [Lightmapping.ClearLightingDataAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.ClearLightingDataAsset.html).
* * *
