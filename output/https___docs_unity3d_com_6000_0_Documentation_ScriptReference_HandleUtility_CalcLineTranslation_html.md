* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.CalcLineTranslation.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).CalcLineTranslation
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
public static float CalcLineTranslation([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) src, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) dest, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) srcPosition, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) constraintDir); 
### Parameters
Parameter | Description  
---|---  
src | The source point of the drag.  
dest | The destination point of the drag.  
srcPosition | The 3D position the dragged object had at `src` ray.  
constraintDir | Normalized 3D direction of constrained movement.  
### Returns
**float** The distance travelled along constraintDir. 
### Description
Map a mouse drag onto a movement along a line in 3D space.
Certain types of Handles (such as arrows) involve movement along a line in 3D space. For example, the Transform's position arrows move the object along its local X, Y or Z axis as the mouse is dragged. The CalcLineTranslation function converts the movement of the mouse into constrained movement along a 3D line in the familiar way used by Unity's built-in tools.
* * *
