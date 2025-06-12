* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeMultipleScenes.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).BakeMultipleScenes
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
public static void BakeMultipleScenes(string[] paths); 
### Parameters
Parameter | Description  
---|---  
paths | The path of the Scenes that should be baked.  
### Description
Bakes an array of Scenes.
This loads all Scenes and then builds all lightmaps, Reflection Probes and Enlighten Realtime Global Illumination data. The function automatically splits baked data by Scene. This means you can bake lightmaps for two adjacent levels and have light and shadows cast onto objects in level A affect objects in level B.  
  
Enlighten system data automatically connects neighboring systems when it is additively loaded, thus bounce lighting can flow from one Scene to another.  
  
A single LightProbe asset is generated for all Scenes. Hence for the time being, lightprobes always take as much memory as there are lightprobes in all levels that are baked together.  
  
Only one ambient probe & default sky probe will be baked and assigned to each Scene.  
  
Multiple Lightmapsnapshot objects containing the data for each Scene are written into a single file in "MyScene/LightmapSnapshot.asset". At build time this data will also be automatically split as well, hence if you bake multiple Scenes but then only deploy one Scene then only the lightmap data for that Scene will be deployed.
* * *
