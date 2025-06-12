* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.QueryIndices.html

#  [CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html).QueryIndices
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
public int QueryIndices(bool visible, int[] result, int firstIndex); 
## Declaration
public int QueryIndices(int distanceIndex, int[] result, int firstIndex); 
## Declaration
public int QueryIndices(bool visible, int distanceIndex, int[] result, int firstIndex); 
### Parameters
Parameter | Description  
---|---  
visible | True if only visible spheres should be retrieved; false if only invisible spheres should be retrieved.  
distanceIndex | The distance band that retrieved spheres must be in.  
result | An array that will be filled with the retrieved sphere indices.  
firstIndex | The index of the sphere to begin searching at.  
### Returns
**int** The number of sphere indices found and written into the result array. 
### Description
Retrieve the indices of spheres that have particular visibility and/or distance states.
Use the overload that corresponds to the state properties you are interested in. For example, if you want to retrieve visible spheres in any distance band, use the overload that takes a 'visible' parameter but does not have a 'distanceIndex' parameter.  
  
The length of the result array is used to limit the number of spheres checked. If you provide a result array of length 20, and a firstIndex of 10, then the query will only examine spheres 10 through 30 to see if they meet the given visibility and/or distance constraints.
* * *
