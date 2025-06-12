* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.IsVisible.html

#  [CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html).IsVisible
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
public bool IsVisible(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the bounding sphere.  
### Returns
**bool** True if the sphere is visible; false if it is invisible. 
### Description
Returns true if the bounding sphere at index is currently visible from any of the contributing cameras.
Note that this method uses the most recently computed visibility states. Visibility is updated immediately before rendering, so using this method in Update/LateUpdate will provide results based on calculations from the previous frame.
* * *
