* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html

# Gizmos
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Gizmos are used to give visual debugging or setup aids in the Scene view.
All gizmo drawing has to be done in either [MonoBehaviour.OnDrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmos.html) or [MonoBehaviour.OnDrawGizmosSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmosSelected.html) functions of the script. [MonoBehaviour.OnDrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmos.html) is called when the Scene view or Game view is repainted. All gizmos that render in [MonoBehaviour.OnDrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmos.html) are pickable. [MonoBehaviour.OnDrawGizmosSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmosSelected.html) is called only if the object the script is attached to is selected.
### Static Properties
Property | Description  
---|---  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) | Sets the Color of the gizmos that are drawn next.  
[exposure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-exposure.html) | Set a texture that contains the exposure correction for LightProbe gizmos. The value is sampled from the red channel in the middle of the texture.  
[matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) | Sets the Matrix4x4 that the Unity Editor uses to draw Gizmos.  
[probeSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-probeSize.html) | Set a scale for Light Probe gizmos. This scale will be used to render the spherical harmonic preview spheres.  
### Static Methods
Method | Description  
---|---  
[CalculateLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.CalculateLOD.html) | Determines the appropriate level of detail for a gizmo in the Scene view at a specified position with a specified radius.  
[DrawCube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawCube.html) | Draw a solid box at center with size.  
[DrawFrustum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawFrustum.html) | Draw a camera frustum using the currently set Gizmos.matrix for its location and rotation.  
[DrawGUITexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawGUITexture.html) | Draw a texture in the Scene.  
[DrawIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawIcon.html) | Draw an icon at a position in the Scene view.  
[DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html) | Draws a line starting at from towards to.  
[DrawLineList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineList.html) | Draws multiple lines between pairs of points.  
[DrawLineStrip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineStrip.html) | Draws a line between each point in the supplied span.  
[DrawMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawMesh.html) | Draws a mesh.  
[DrawRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawRay.html) | Draws a ray starting at from to from + direction.  
[DrawSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html) | Draws a solid sphere with center and radius.  
[DrawWireCube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireCube.html) | Draw a wireframe box with center and size.  
[DrawWireMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireMesh.html) | Draws a wireframe mesh.  
[DrawWireSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireSphere.html) | Draws a wireframe sphere with center and radius.  
* * *
