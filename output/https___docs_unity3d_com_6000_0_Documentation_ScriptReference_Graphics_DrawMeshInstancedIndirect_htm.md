* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstancedIndirect.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).DrawMeshInstancedIndirect
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
public static void DrawMeshInstancedIndirect([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) bufferWithArgs, int argsOffset = 0, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties = null, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows = ShadowCastingMode.On, bool receiveShadows = true, int layer = 0, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = null, [Rendering.LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) lightProbeUsage = LightProbeUsage.BlendProbes, [LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html) lightProbeProxyVolume = null); 
## Declaration
public static void DrawMeshInstancedIndirect([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) bufferWithArgs, int argsOffset = 0, [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties = null, [Rendering.ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) castShadows = ShadowCastingMode.On, bool receiveShadows = true, int layer = 0, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = null, [Rendering.LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) lightProbeUsage = LightProbeUsage.BlendProbes, [LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html) lightProbeProxyVolume = null); 
### Parameters
Parameter | Description  
---|---  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to draw.  
submeshIndex | Which subset of the mesh to draw. This applies only to meshes that are composed of several materials.  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) to use.  
bounds | The bounding volume surrounding the instances you intend to draw.  
bufferWithArgs | The GPU buffer containing the arguments for how many instances of this mesh to draw.  
argsOffset | The byte offset into the buffer, where the draw arguments start.  
properties | Additional material properties to apply. See [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).  
castShadows | Determines whether the mesh can cast shadows.  
receiveShadows | Determines whether the mesh can receive shadows.  
layer |  [Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) to use.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be drawn in the given Camera only.  
lightProbeUsage |  [LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) for the instances.  
### Description
This function is now obsolete. Use [Graphics.RenderMeshIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html) instead. Draws the same mesh multiple times using GPU instancing.
This function only works on platforms that support [compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).  
  
Similar to [Graphics.DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstanced.html), this function draws many instances of the same mesh, but unlike that method, the arguments for how many instances to draw come from `bufferWithArgs`.  
  
Use this function in situations where you want to draw the same mesh for a particular amount of times using an instanced shader. Meshes are not further culled by the view frustum or baked occluders, nor sorted for transparency or z efficiency.  
  
Buffer with arguments, `bufferWithArgs`, has to have five integer numbers at given `argsOffset` offset: index count per instance, instance count, start index location, base vertex location, start instance location.  
  
Unity only needs the submeshIndex argument if submeshes within the mesh have different topologies (e.g. Triangles and Lines). Otherwise, all the information about which submesh to draw comes from the bufferWithArgs argument.  
  
Here is a script that can be used to draw many instances of the same mesh:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    public int instanceCount = 100000;
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) instanceMesh;
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) instanceMaterial;
    public int subMeshIndex = 0;  
  
    private int cachedInstanceCount = -1;
    private int cachedSubMeshIndex = -1;
    private ComputeBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) positionBuffer;
    private ComputeBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) argsBuffer;
    private uint[] args = new uint[5] { 0, 0, 0, 0, 0 };  
  
    void Start() {
        argsBuffer = new ComputeBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html)(1, args.Length * sizeof(uint), ComputeBufferType.IndirectArguments[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.IndirectArguments.html));
        UpdateBuffers();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() {
        // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) starting position buffer
        if (cachedInstanceCount != instanceCount || cachedSubMeshIndex != subMeshIndex)
            UpdateBuffers();  
  
        // Pad input
        if (Input.GetAxisRaw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxisRaw.html)("Horizontal") != 0.0f)
            instanceCount = (int)Mathf.Clamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp.html)(instanceCount + Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") * 40000, 1.0f, 5000000.0f);  
  
        // Render
        Graphics.DrawMeshInstancedIndirect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshInstancedIndirect.html)(instanceMesh, subMeshIndex, instanceMaterial, new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(100.0f, 100.0f, 100.0f)), argsBuffer);
    }  
  
    void OnGUI() {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(265, 25, 200, 30), "Instance Count: " + instanceCount.ToString());
        instanceCount = (int)GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 20, 200, 30), (float)instanceCount, 1.0f, 5000000.0f);
    }  
  
    void UpdateBuffers() {
        // Ensure submesh index is in range
        if (instanceMesh != null)
            subMeshIndex = Mathf.Clamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp.html)(subMeshIndex, 0, instanceMesh.subMeshCount - 1);  
  
        // Positions
        if (positionBuffer != null)
            positionBuffer.Release();
        positionBuffer = new ComputeBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html)(instanceCount, 16);
        Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)[] positions = new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)[instanceCount];
        for (int i = 0; i < instanceCount; i++) {
            float angle = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.0f, Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html) * 2.0f);
            float distance = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(20.0f, 100.0f);
            float height = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-2.0f, 2.0f);
            float size = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.05f, 0.25f);
            positions[i] = new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(angle) * distance, height, Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(angle) * distance, size);
        }
        positionBuffer.SetData(positions);
        instanceMaterial.SetBuffer("positionBuffer", positionBuffer);  
  
        // Indirect args
        if (instanceMesh != null) {
            args[0] = (uint)instanceMesh.GetIndexCount(subMeshIndex);
            args[1] = (uint)instanceCount;
            args[2] = (uint)instanceMesh.GetIndexStart(subMeshIndex);
            args[3] = (uint)instanceMesh.GetBaseVertex(subMeshIndex);
        }
        else
        {
            args[0] = args[1] = args[2] = args[3] = 0;
        }
        argsBuffer.SetData(args);  
  
        cachedInstanceCount = instanceCount;
        cachedSubMeshIndex = subMeshIndex;
    }  
  
    void OnDisable() {
        if (positionBuffer != null)
            positionBuffer.Release();
        positionBuffer = null;  
  
        if (argsBuffer != null)
            argsBuffer.Release();
        argsBuffer = null;
    }
}

```

Here is a surface shader that can be used with the example script above:
```
          Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "Instanced/InstancedSurfaceShader" {
    Properties {
        _MainTex ("Albedo (RGB)", 2D) = "white" {}
        _Glossiness ("Smoothness", Range(0,1)) = 0.5
        _Metallic ("Metallic", Range(0,1)) = 0.0
    }
    SubShader {
        Tags { "RenderType"="Opaque" }
        LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html) 200  
  
        CGPROGRAM
        // Physically based Standard lighting model
        #pragma surface surf Standard addshadow fullforwardshadows
        #pragma multi_compile_instancing
        #pragma instancing_options procedural:setup  
  
        sampler2D _MainTex;  
  
        struct Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) {
            float2 uv_MainTex;
        };  
  
    #ifdef UNITY_PROCEDURAL_INSTANCING_ENABLED
        StructuredBuffer<float4> positionBuffer;
    #endif  
  
        void rotate2D(inout float2 v, float r)
        {
            float s, c;
            sincos(r, s, c);
            v = float2(v.x * c - v.y * s, v.x * s + v.y * c);
        }  
  
        void setup()
        {
        #ifdef UNITY_PROCEDURAL_INSTANCING_ENABLED
            float4 data = positionBuffer[unity_InstanceID];  
  
            float rotation = data.w * data.w * _Time.y * 0.5f;
            rotate2D(data.xz, rotation);  
  
            unity_ObjectToWorld._11_21_31_41 = float4(data.w, 0, 0, 0);
            unity_ObjectToWorld._12_22_32_42 = float4(0, data.w, 0, 0);
            unity_ObjectToWorld._13_23_33_43 = float4(0, 0, data.w, 0);
            unity_ObjectToWorld._14_24_34_44 = float4(data.xyz, 1);
            unity_WorldToObject = unity_ObjectToWorld;
            unity_WorldToObject._14_24_34 *= -1;
            unity_WorldToObject._11_22_33 = 1.0f / unity_WorldToObject._11_22_33;
        #endif
        }  
  
        half _Glossiness;
        half _Metallic;  
  
        void surf (Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) IN, inout SurfaceOutputStandard o) {
            fixed4 c = tex2D (_MainTex, IN.uv_MainTex);
            o.Albedo = c.rgb;
            o.Metallic = _Metallic;
            o.Smoothness = _Glossiness;
            o.Alpha = c.a;
        }
        ENDCG
    }
    FallBack "Diffuse"
}

```

Here is a custom shader that can be used with the example script above:
```
          Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "Instanced/InstancedShader" {
    Properties {
        _MainTex ("Albedo (RGB)", 2D) = "white" {}
    }
    SubShader {  
  
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html) {  
  
            Tags {"LightMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.LightMode.html)"="ForwardBase"}  
  
            CGPROGRAM  
  
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_fwdbase nolightmap nodirlightmap nodynlightmap novertexlight
            #pragma target 4.5  
  
            #include "UnityCG.cginc"
            #include "UnityLightingCommon.cginc"
            #include "AutoLight.cginc"  
  
            sampler2D _MainTex;  
  
        #if SHADER_TARGET >= 45
            StructuredBuffer<float4> positionBuffer;
        #endif  
  
            struct v2f
            {
                float4 pos : SV_POSITION;
                float2 uv_MainTex : TEXCOORD0;
                float3 ambient : TEXCOORD1;
                float3 diffuse : TEXCOORD2;
                float3 color : TEXCOORD3;
                SHADOW_COORDS(4)
            };  
  
            void rotate2D(inout float2 v, float r)
            {
                float s, c;
                sincos(r, s, c);
                v = float2(v.x * c - v.y * s, v.x * s + v.y * c);
            }  
  
            v2f vert (appdata_full v, uint instanceID : SV_InstanceID)
            {
            #if SHADER_TARGET >= 45
                float4 data = positionBuffer[instanceID];
            #else
                float4 data = 0;
            #endif  
  
                float rotation = data.w * data.w * _Time.x * 0.5f;
                rotate2D(data.xz, rotation);  
  
                float3 localPosition = v.vertex.xyz * data.w;
                float3 worldPosition = data.xyz + localPosition;
                float3 worldNormal = v.normal;  
  
  
  
                float3 ndotl = saturate(dot(worldNormal, _WorldSpaceLightPos0.xyz));
                float3 ambient = ShadeSH9(float4(worldNormal, 1.0f));
                float3 diffuse = (ndotl * _LightColor0.rgb);
                float3 color = v.color;  
  
                v2f o;
                o.pos = mul(UNITY_MATRIX_VP, float4(worldPosition, 1.0f));
                o.uv_MainTex = v.texcoord;
                o.ambient = ambient;
                o.diffuse = diffuse;
                o.color = color;
                TRANSFER_SHADOW(o)
                return o;
            }  
  
            fixed4 frag (v2f i) : SV_Target
            {
                fixed shadow = SHADOW_ATTENUATION(i);
                fixed4 albedo = tex2D(_MainTex, i.uv_MainTex);
                float3 lighting = i.diffuse * shadow + i.ambient;
                fixed4 output = fixed4(albedo.rgb * i.color * lighting, albedo.w);
                UNITY_APPLY_FOG(i.fogCoord, output);
                return output;
            }  
  
            ENDCG
        }
    }
}

```

* * *
