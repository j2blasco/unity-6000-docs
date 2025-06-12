* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetColors.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetColors
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public void GetColors(List<Color> colors); 
## Declaration
public void GetColors(List<Color32> colors); 
### Parameters
Parameter | Description  
---|---  
colors | A list of vertex colors to populate.  
### Description
Gets the vertex colors of the Mesh.
The color at each index corresponds to the vertex with the same index.  
  
Use this method instead of [colors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors.html) or [colors32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors32.html) if you control the life cycle of the list passed in and you want to avoid allocating a new array with every access.  
  
Additional resources: [AcquireReadOnlyMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.AcquireReadOnlyMeshData.html) function.
* * *
