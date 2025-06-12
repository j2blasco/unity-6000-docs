* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.Frame.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).Frame
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
public bool Frame([Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, bool instant); 
### Parameters
Parameter | Description  
---|---  
bounds | The bounds to frame in the Scene view.  
instant | Set to true to immediately frame the camera. Set to false to animate the action.  
### Returns
**bool** Returns true if the given bounds can be encompassed in the Scene view. Returns false otherwise. 
### Description
Frames the given bounds in the Scene view.
* * *
