* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DSlice.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawTexture3DSlice
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
public static void DrawTexture3DSlice([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slicePositions, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filterMode = FilterMode.Bilinear, bool useColorRamp = false, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) customColorRamp = null); 
### Parameters
Parameter | Description  
---|---  
texture | The volumetric texture to draw.  
slicePositions | The positions of the texture sampling planes.  
filterMode | Sets the texture filtering mode to use.  
useColorRamp | Enables color ramp visualization.  
customColorRamp | The custom gradient that Unity uses as a color ramp. If this is not specified, Unity uses [Google Turbo color ramp](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html).  
### Description
Draws a 3D texture using Slice rendering mode in 3D space.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/3DTextureHandleHeadSlice.png)   
_Head scan rendered in slice mode with a custom gradient._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class Reference : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) texture;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) slicePositions;
    public FilterMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filterMode;
    public bool useColorRamp;
    public bool useCustomColorRamp;  
  
    // We should initialize this gradient before using it as a custom color ramp
    public Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) customColorRampGradient;
}  
  
[CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(Reference))]
public class Handle : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    private void OnSceneViewGUI(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) sv)
    {
        Object[] objects = targets;
        foreach (var obj in objects)
        {
            Reference reference = obj as Reference;
            if (reference != null && reference.texture != null)
            {
                Handles.matrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html) = reference.transform.localToWorldMatrix;
                Handles.DrawTexture3DSlice[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DSlice.html)(reference.texture, reference.slicePositions, reference.filterMode,
                    reference.useColorRamp, reference.useCustomColorRamp ? reference.customColorRampGradient : null);
            }
        }
    }  
  
    void OnEnable()
    {
        SceneView.duringSceneGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) += OnSceneViewGUI;
    }  
  
    void OnDisable()
    {
        SceneView.duringSceneGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) -= OnSceneViewGUI;
    }
}

```

Additional resources: [Handles.DrawTexture3DSDF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DSDF.html), [Handles.DrawTexture3DVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DVolume.html), [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html), [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html).
* * *
