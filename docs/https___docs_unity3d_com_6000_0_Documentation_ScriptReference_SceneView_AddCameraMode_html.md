* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AddCameraMode.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).AddCameraMode
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
public static [SceneView.CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) AddCameraMode(string name, string section); 
### Parameters
Parameter | Description  
---|---  
name | The name for the new mode.  
section | The section in which the new mode will be added. This can be an existing or new section.  
### Returns
**CameraMode** A CameraMode with the provided name and section. 
### Description
Add a custom camera mode to the Scene view camera mode list.
When a user-defined mode is selected, the Scene view will render as though the "shaded" mode is selected.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Using a ScriptableSingleton lets us initialize and cleanup any managed resources with OnEnable and OnDisable.
class CustomCameraMode : ScriptableSingleton<CustomCameraMode>
{
    // Initialize an instance of this class when the editor loads.
    [InitializeOnLoadMethod]
    static void Init() => _ = instance;  
  
    const string k_Name = "Positions as Colors";
    const string k_Section = "Miscellaneous";
    Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) m_ReplacementShader;
    Dictionary<SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html), bool> m_Active = new Dictionary<SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html), bool>();  
  
    void OnEnable()
    {
        // Make sure to only call AddCameraMode once. This adds the camera mode to all existing and future SceneViews.
        SceneView.AddCameraMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AddCameraMode.html)(k_Name, k_Section);  
  
        // Custom modes are implemented through replacement shaders. We set the replacement shader during repaint events
        // in the OnSceneGUI callback.
        SceneView.duringSceneGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) += OnSceneGUI;  
  
        // Create a shader in your project with code below this example.
        m_ReplacementShader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Unlit/PositionAsColor");
    }  
  
    // If any managed resources are created in OnEnable, they should be cleaned up in OnDisable.
    void OnDisable()
    {
        SceneView.duringSceneGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) -= OnSceneGUI;
    }  
  
    void OnSceneGUI(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) view)
    {
        if (Event.current.type != EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html))
            return;  
  
        // When the active camera mode changes, we need to update the replacement shader. The replacement shader and
        // tag are serialized for each scene view, and do not need to be re-applied every frame or after domain reloads.
        // Alternatively, you can make use of the `SceneView.onCameraModeChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-onCameraModeChanged.html)` event to update the replacement shader.
        if(!m_Active.TryGetValue(view, out var wasActive))
            m_Active[view] = wasActive = false;  
  
        var isActive = view.cameraMode.drawMode == DrawCameraMode.UserDefined[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.UserDefined.html)
             && view.cameraMode.name == k_Name
             && view.cameraMode.section== k_Section;  
  
        if (wasActive == isActive)
            return;  
  
        m_Active[view] = isActive;  
  
        if(isActive)
            view.SetSceneViewShaderReplace(m_ReplacementShader, string.Empty);
        else
            view.SetSceneViewShaderReplace(null, null);
    }
}

```

The source code for the shader used in the sample above is an example.
```
          Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "Unlit/PositionAsColor"
{
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html) 100  
  
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag  
  
            #include "UnityCG.cginc"  
  
            struct appdata
            {
                float4 vertex : POSITION;
            };  
  
            struct v2f
            {
                float4 vertex : SV_POSITION;
                float4 color  : COLOR;
            };  
  
            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.color = float4((normalize(v.vertex.xyz)+1)*.5, 1);
                return o;
            }  
  
            fixed4 frag (v2f i) : SV_Target
            {
                return i.color;
            }
            ENDCG
        }
    }
}

```

* * *
