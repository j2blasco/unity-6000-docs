* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.SetActiveVertexStreams.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).SetActiveVertexStreams
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
public void SetActiveVertexStreams(List<ParticleSystemVertexStream> streams); 
### Parameters
Parameter | Description  
---|---  
streams | The new array of enabled vertex streams.  
### Description
Enables a set of Vertex Shader streams on the [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).
Additional resources: [ParticleSystemRenderer.GetActiveVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.GetActiveVertexStreams.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections.Generic;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {  
  
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) psr;
    private List<Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)> customData = new List<Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)>();
    public float minDist = 30.0f;  
  
    void Start() {  
  
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        psr = GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>();  
  
        // emit in a sphere with no speed
        var main = ps.main;
        main.startSpeedMultiplier = 0.0f;
        main.simulationSpace = ParticleSystemSimulationSpace.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSimulationSpace.World.html); // so our particle positions don't require any extra transformation, to compare with the mouse position
        var emission = ps.emission;
        emission.rateOverTimeMultiplier = 200.0f;
        var shape = ps.shape;
        shape.shapeType = ParticleSystemShapeType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemShapeType.Sphere.html);
        shape.radius = 4.0f;
        psr.sortMode = ParticleSystemSortMode.YoungestInFront[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSortMode.YoungestInFront.html);  
  
        // send custom data to the shader
        psr.SetActiveVertexStreams(new List<ParticleSystemVertexStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.html)>(new ParticleSystemVertexStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.html)[] { ParticleSystemVertexStream.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Position.html), ParticleSystemVertexStream.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Normal.html), ParticleSystemVertexStream.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Color.html), ParticleSystemVertexStream.UV[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.UV.html), ParticleSystemVertexStream.Custom1X[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom1X.html) }));
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() {  
  
        Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) mainCam = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);  
  
        ps.GetCustomParticleData(customData, ParticleSystemCustomData.Custom1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomData.Custom1.html));  
  
        // If you know the particle count, or have a reasonable maxParticles threshold, consider caching
        // this array instead of reallocating it on every frame, to avoid per-frame garbage.
        int particleCount = ps.particleCount;
        ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)[] particles = new ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)[particleCount];  
  
        ps.GetParticles(particles);  
  
        for (int i = 0; i < particles.Length; i++)
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) sPos = mainCam.WorldToScreenPoint(particles[i].position);  
  
            // set custom data to 1, if close enough to the mouse
            if (Vector2.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Distance.html)(sPos, Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html)) < minDist)
            {
                customData[i] = new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(1, 0, 0, 0);
            }
            // otherwise, fade the custom data back to 0
            else
            {
                float particleLife = particles[i].remainingLifetime / ps.main.startLifetimeMultiplier;  
  
                if (customData[i].x > 0)
                {
                    float x = customData[i].x;
                    x = Mathf.Max[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Max.html)(x - Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), 0.0f);
                    customData[i] = new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(x, 0, 0, 0);
                }
            }
        }  
  
        ps.SetCustomParticleData(customData, ParticleSystemCustomData.Custom1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomData.Custom1.html));
    }  
  
    void OnGUI() {  
  
        minDist = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 40, 100, 30), minDist, 0.0f, 100.0f);
    }
}

```

Here is an example of a custom Shader that you can use with the above script:
```
          Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "Particles/CustomVertexStream" {
Properties {
    _TintColor ("Tint Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)", Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)) = (0.5,0.5,0.5,0.5)
    _MainTex ("Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)", 2D) = "white" {}
    _OffsetValue("Offset Value", Range(0,1)) = 0.4
}  
  
Category[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Category.html) {
    Tags { "Queue"="Transparent" "IgnoreProjector"="True" "RenderType"="Transparent" }
    Blend SrcAlpha OneMinusSrcAlpha
    ColorMask RGB
    Cull Off Lighting Off ZWrite Off  
  
    SubShader {
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html) {  
  
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_particles
            #pragma multi_compile_fog  
  
            #include "UnityCG.cginc"  
  
            sampler2D _MainTex;
            fixed4 _TintColor;
            float _OffsetValue;  
  
            struct appdata_t {
                float4 vertex : POSITION;
                float3 normal : NORMAL;
                fixed4 color : COLOR;
                float3 texcoordAndCustom : TEXCOORD0;
            };  
  
            struct v2f {
                float4 vertex : SV_POSITION;
                fixed4 color : COLOR;
                float2 texcoord : TEXCOORD0;
                float customData : TEXCOORD1;
                UNITY_FOG_COORDS(2)
            };  
  
            float4 _MainTex_ST;  
  
            v2f vert (appdata_t v)
            {
                v.vertex.y = lerp(v.vertex.y, v.vertex.y + _OffsetValue, v.texcoordAndCustom.z);  
  
                v2f o;
                o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);  
  
                float4 offsetX = float4(-1, 1, 1, -1);
                float4 offsetY = float4(1, 1, -1, -1);  
  
                o.color = v.color;
                o.texcoord = TRANSFORM_TEX(v.texcoordAndCustom.xy,_MainTex);
                o.customData = v.texcoordAndCustom.z;
                UNITY_TRANSFER_FOG(o,o.vertex);  
  
                return o;
            }  
  
            fixed4 frag (v2f i) : SV_Target
            {
                fixed4 col = 2.0f * i.color * _TintColor * tex2D(_MainTex, i.texcoord);
                fixed4 col2 = fixed4(i.customData, 0, 0, col.a);
                fixed4 final = lerp(col, col*col2, i.customData.x);  
  
                UNITY_APPLY_FOG(i.fogCoord, final);
                return final;
            }
            ENDCG
        }
    }
}
}

```

* * *
