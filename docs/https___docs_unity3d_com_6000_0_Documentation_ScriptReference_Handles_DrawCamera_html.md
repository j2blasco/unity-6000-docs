* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawCamera.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawCamera
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
public static void DrawCamera([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
## Declaration
public static void DrawCamera([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, [DrawCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.html) drawMode = UnityEditor.DrawCameraMode.Normal); 
### Parameters
Parameter | Description  
---|---  
position | The area to draw the camera within in GUI coordinates.  
camera | The camera to draw.  
drawMode | How the camera is drawn (textured, wireframe, etc.).  
### Description
Draws a camera inside a rectangle.
This function also sets [Camera.current](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-current.html) to `camera`. It sets the camera's pixelRect to `position`, but in screen coordinates. This might be different from GUI coordinates if you are using a high DPI display.  
  
**Note:** Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) where you might want to have constant screen-sized handles.  
  
See Also [EditorGUIUtility.pixelsPerPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-pixelsPerPoint.html).
* * *
