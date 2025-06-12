* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).BuildRayTracingAccelerationStructure
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
public void BuildRayTracingAccelerationStructure([Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) accelerationStructure); 
## Declaration
public void BuildRayTracingAccelerationStructure([Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) accelerationStructure, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relativeOrigin); 
## Declaration
public void BuildRayTracingAccelerationStructure([Rendering.RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) accelerationStructure, [Rendering.RayTracingAccelerationStructure.BuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.BuildSettings.html) buildSettings); 
### Parameters
Parameter | Description  
---|---  
accelerationStructure | The [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) to be generated.  
relativeOrigin | The relative origin of ray tracing instances. The default value is [Vector3.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html). To use camera-relative ray-tracing, set this parameter to the position of the camera.  
buildSettings | The [BuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.BuildSettings.html) to use.  
### Description
Adds a command to build the [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) to be used in a ray tracing dispatch or when using inline ray tracing (ray queries).
To ensure that the acceleration structure is up to date, call this method before using the acceleration structure in ray tracing shaders (for example before a [CommandBuffer.DispatchRays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DispatchRays.html) call) or when using inline ray tracing.  
  
In the following example, the `Update` method uses a compute shader dispatch to modify the vertex positions of a mesh instance, then the [RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) is rebuilt.
```
using Unity.Collections;
using UnityEngine;
using UnityEngine.Rendering;  
  
public class RayTracingInstanceManager : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) instanceMaterial;
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) vertexAnimationShader;
    public RayTracingShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) rayTracingShader;  
  
    private RayTracingAccelerationStructure[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) rtas;
    private CommandBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) cmd;
    private RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) rayTracingOutput;
    private uint cameraWidth = 0;
    private uint cameraHeight = 0;
    private uint meshResolution = 32;
    private Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) instanceMesh;  
  
    void Start()
    {
        // Create command buffer
        cmd = new CommandBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html)();
        cmd.name = "Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) Tracing Setup";  
  
        InitializeRayTracing();
    }  
  
    private NativeArray<uint> CreateIndexArray(uint resolution)
    {
        uint indexCount = 2 * 3 * resolution * resolution;
        uint[] indices = new uint[indexCount];  
  
        int index = 0;  
  
        for (uint i = 0; i < resolution; i++)
        {
            for (uint j = 0; j < resolution; j++)
            {
                indices[index++] = i * (resolution + 1) + j;
                indices[index++] = (i + 1) * (resolution + 1) + j;
                indices[index++] = (i + 1) * (resolution + 1) + j + 1;  
  
                indices[index++] = i * (resolution + 1) + j;
                indices[index++] = (i + 1) * (resolution + 1) + j + 1;
                indices[index++] = i * (resolution + 1) + j + 1;
            }
        }  
  
        return new NativeArray<uint>(indices, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
    }  
  
    struct Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)
    {
        public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position;
    }  
  
    private NativeArray<Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)> CreateVertexArray(uint resolution)
    {
        uint vertexCount = (resolution + 1) * (resolution + 1);
        Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)[] vertices = new Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)[vertexCount];  
  
        float invResolution = 1.0f / (float)resolution;
        float step = 2.0f * invResolution;
        int vertexIndex = 0;
        float posZ = -1.0f;  
  
        for (uint z = 0; z <= resolution; z++)
        {
            float posX = -1.0f;  
  
            for (uint x = 0; x <= resolution; x++)
            {
                vertices[vertexIndex].position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(posX, 0, posZ);  
  
                vertexIndex++;
                posX += step;
            }
            posZ += step;
        }  
  
        return new NativeArray<Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)>(vertices, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
    }  
  
    void InitializeRayTracing()
    {
        // Set up acceleration structure
        RayTracingAccelerationStructure.Settings settings = new RayTracingAccelerationStructure.Settings
        {
            managementMode = RayTracingAccelerationStructure.ManagementMode.Manual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.ManagementMode.Manual.html),
            layerMask = -1
        };
        rtas = new RayTracingAccelerationStructure[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html)(settings);
        // Create base mesh on GPU
        instanceMesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();  
  
        if (SystemInfo.supportsComputeShaders[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html))
        {
            instanceMesh.vertexBufferTarget |= GraphicsBuffer.Target.Raw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html);
            instanceMesh.indexBufferTarget |= GraphicsBuffer.Target.Raw[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Raw.html);
        }  
  
        using (NativeArray<Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html)> varray = CreateVertexArray(meshResolution))
        {
            instanceMesh.SetVertexBufferParams(varray.Length, new VertexAttributeDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html)(VertexAttribute.Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.Position.html), VertexAttributeFormat.Float32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.Float32.html), 3));
            instanceMesh.SetVertexBufferData(varray, 0, 0, varray.Length);
        }  
  
        using (NativeArray<uint> iarray = CreateIndexArray(meshResolution))
        {
            instanceMesh.SetIndexBufferParams(iarray.Length, IndexFormat.UInt32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.UInt32.html));
            instanceMesh.SetIndexBufferData(iarray, 0, 0, iarray.Length);
            instanceMesh.SetSubMesh(0, new SubMeshDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html)(0, iarray.Length));
        }  
  
        RayTracingMeshInstanceConfig[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingMeshInstanceConfig.html) gpuMeshInstance = new RayTracingMeshInstanceConfig[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingMeshInstanceConfig.html)(instanceMesh, 0, instanceMaterial);  
  
        // Make the acceleration structure update every time we call RayTracingAccelerationStructure.Build[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Build.html) or CommandBuffer.BuildRayTracingAccelerationStructure[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html).
        gpuMeshInstance.dynamicGeometry = true;  
  
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix = Matrix4x4.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html);
        matrix.SetTRS(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html));  
  
        rtas.AddInstance(gpuMeshInstance, matrix);
    }  
  
    void CreateResources()
    {
        if (cameraWidth != Camera.main.pixelWidth || cameraHeight != Camera.main.pixelHeight)
        {
            if (rayTracingOutput != null)
                rayTracingOutput.Release();
            rayTracingOutput = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)(Camera.main.pixelWidth, Camera.main.pixelHeight, 0, RenderTextureFormat.ARGBHalf[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGBHalf.html));
            rayTracingOutput.enableRandomWrite = true;
            rayTracingOutput.Create();
            cameraWidth = (uint)Camera.main.pixelWidth;
            cameraHeight = (uint)Camera.main.pixelHeight;
        }
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (vertexAnimationShader == null)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html): Compute shader is missing. Assign a compute shader to the vertexAnimationShader property.");
            return;
        }  
  
        GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) vertexBuffer = instanceMesh.GetVertexBuffer(0);
        cmd.SetComputeBufferParam(vertexAnimationShader, 0, "vertexBuffer", vertexBuffer);  
  
        cmd.SetComputeFloatParam(vertexAnimationShader, "realtimeSinceStartup", Time.realtimeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html));
        cmd.SetComputeIntParam(vertexAnimationShader, "vertexCount", vertexBuffer.count);
        cmd.SetComputeIntParam(vertexAnimationShader, "vertexSizeInBytes", vertexBuffer.stride);  
  
        if (vertexBuffer.stride % 4 != 0)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) stride must be a multiple of 4.");  
  
        uint kernelGroupSizeX, kernelGroupSizeY, kernelGroupSizeZ;
        vertexAnimationShader.GetKernelThreadGroupSizes(0, out kernelGroupSizeX, out kernelGroupSizeY, out kernelGroupSizeZ);  
  
        int threadGroupsX = (int)(instanceMesh.vertexCount + kernelGroupSizeX - 1) / (int)kernelGroupSizeX;
        cmd.DispatchCompute(vertexAnimationShader, 0, threadGroupsX, 1, 1);  
  
        vertexBuffer.Dispose();  
  
        // Re-build acceleration to take into account modified mesh geometry.
        cmd.BuildRayTracingAccelerationStructure(rtas);
        // The command buffer will be executed in the next OnRenderImage
    }  
  
    [ImageEffectOpaque[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectOpaque.html)]
    void OnRenderImage(RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) src, RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) dest)
    {
        if (!SystemInfo.supportsRayTracing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRayTracing.html) || !rayTracingShader)
        {
            Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Warning: The Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) Tracing API is not supported by this GPU or by the current graphics API.");
            Graphics.Blit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html)(src, dest);
            return;
        }
        CreateResources();
        cmd.SetRayTracingShaderPass(rayTracingShader, "Test");
        // Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html)
        cmd.SetRayTracingAccelerationStructure(rayTracingShader, Shader.PropertyToID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html)("g_AccelStruct"), rtas);
        cmd.SetRayTracingMatrixParam(rayTracingShader, Shader.PropertyToID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html)("g_InvViewMatrix"), Camera.main.cameraToWorldMatrix);
        cmd.SetGlobalVector(Shader.PropertyToID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html)("g_CameraPos"), Camera.main.transform.position);
        // Output
        cmd.SetRayTracingTextureParam(rayTracingShader, Shader.PropertyToID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html)("g_Output"), rayTracingOutput);
        // Execute the raytracing shader
        cmd.DispatchRays(rayTracingShader, "MainRayGenShader", cameraWidth, cameraHeight, 1);
        // Execute command buffer
        Graphics.ExecuteCommandBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBuffer.html)(cmd);
        cmd.Clear();
        Graphics.Blit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html)(rayTracingOutput, dest);
    }  
  
    void OnDisable()
    {
        // Cleanup
        if (rtas != null)
        {
            rtas.Dispose();
            rtas = null;
        }
        if (instanceMesh != null)
        {
            DestroyImmediate(instanceMesh);
            instanceMesh = null;
        }
        if (cmd != null)
        {
            cmd.Release();
            cmd = null;
        }
        if (rayTracingOutput != null)
        {
            rayTracingOutput.Release();
            rayTracingOutput = null;
        }
    }
}
```

Additional resources: [SetRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetRayTracingAccelerationStructure.html), [SetGlobalRayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalRayTracingAccelerationStructure.html), [DispatchRays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DispatchRays.html), [RayTracingAccelerationStructure.Build](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Build.html).
* * *
