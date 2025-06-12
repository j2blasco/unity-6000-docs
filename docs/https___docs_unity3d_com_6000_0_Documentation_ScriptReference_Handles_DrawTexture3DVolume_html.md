* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DVolume.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawTexture3DVolume
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
public static void DrawTexture3DVolume([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture, float opacity = 1.0f, float qualityModifier = 1.0f, [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) filterMode = FilterMode.Bilinear, bool useColorRamp = false, [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) customColorRamp = null); 
### Parameters
Parameter | Description  
---|---  
texture | The volumetric texture to draw.  
opacity | The non-linear volume opacity modifier. Use this to control the opacity of the visualization. Valid values are 0-1, inclusive. A value of 1 is fully opaque and a value of 0 is fully transparent. The default value is 1.  
qualityModifier | Sets the sample per texture pixel count. Higher values result in a higher quality render. The default value is 1.  
filterMode | Sets the texture filtering mode to use.  
useColorRamp | Enables color ramp visualization.  
customColorRamp | The custom gradient that Unity uses as a color ramp. If this is not specified, Unity uses [Google Turbo color ramp](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html).  
### Description
Draws a 3D texture using Volume rendering mode in 3D space.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/3DTextureHandleTeapotVolume.png)   
_Teapot volume rendered with a gradient that has a transparent black outline._  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/3DTextureHandleFireVolume.png)  
_Noise volume with fire gradient applied._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class Reference : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) texture;
    public float alpha = 1;
    public float quality = 1;
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
                Handles.DrawTexture3DVolume[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DVolume.html)(reference.texture, reference.alpha, reference.quality, reference.filterMode,
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
Additional resources: [Handles.DrawTexture3DSDF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DSDF.html), [Handles.DrawTexture3DSlice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawTexture3DSlice.html), [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html), [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html).
* * *
