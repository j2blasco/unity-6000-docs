* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Tetrahedralize.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).Tetrahedralize
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
public static void Tetrahedralize(Vector3[] positions, out int[] outIndices, out Vector3[] outPositions); 
### Parameters
Parameter | Description  
---|---  
positions | An array of Light Probe positions.  
outIndices | An array that Unity populates with updated Light Probe indices.  
outPositions | An array that Unity populates with updated Light Probe positions.  
### Description
Calculates tetrahderons from positions using Delaunay Tetrahedralization.
This is an Editor-only method for visualizing the tetrahedrons that Unity uses for blending probe lighting.  
  
When you pass an array of Light Probe positions, Unity performs the same calculations as it does when regenerating the tetrahedrons, and populates the out parameters with the results of those calculations:  
  
`outIndices`: every four entries correspond to the vertices of a tetrahedron `outPositions`: indexed in the same order as `outIndices`, containing the positions of the corresponding probes  
  
Unity considers Light Probes at the same position (within some tolerance) as duplicates, and does not include them in the tetrahedralization. When this happens, only the first element is included. As a result, `outPositions` might have fewer elements than `positions`.  
  
Note that this method does not cause Unity to update the tetrahedrons that it uses for Light Probes; use this method only for visualizing the results of such an operation.  
  
Additional resources: [LightProbes.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html), [LightProbes.TetrahedralizeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html), [Light Probes and Scene loading](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html).
* * *
