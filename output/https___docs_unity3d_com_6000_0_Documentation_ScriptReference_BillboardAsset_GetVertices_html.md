* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.GetVertices.html

#  [BillboardAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.html).GetVertices
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardAsset.html "Go to BillboardAsset Component in the Manual")
## Declaration
public Vector2[] GetVertices(); 
## Declaration
public void GetVertices(List<Vector2> vertices); 
### Parameters
Parameter | Description  
---|---  
vertices | The list that receives the array.  
### Description
Get the vertices of the billboard mesh.
Each vertex is a [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) in UV space. The second overload guarantees no memory allocation happening if the list capacity is big enough to hold the data.  
  
Additional resources: [BillboardAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.html), [SetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.SetVertices.html).
* * *
