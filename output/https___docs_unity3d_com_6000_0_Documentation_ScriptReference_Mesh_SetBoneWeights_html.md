* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).SetBoneWeights
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public void SetBoneWeights(NativeArray<byte> bonesPerVertex, NativeArray<BoneWeight1> weights); 
### Parameters
Parameter | Description  
---|---  
bonesPerVertex | Bone count for each vertex in the Mesh.  
weights |  [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) structs for each vertex, sorted by vertex index.  
### Description
Sets the bone weights for the Mesh.
Supports up to 255 bone weights per vertex. The bone weights for each vertex must be sorted with the most significant weights first. Zero weights will be ignored.  
  
The weights may be stored with less precision than the floating point values passed in, so do not expect to get the exact same values back using [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html). The minimum precision used is currently 16-bit normalized integers.  
  
Additional resources: [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html), [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html), [Mesh.GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html) [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
```
using UnityEngine;
using Unity.Collections;  
  
public class MeshSetBoneWeights : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) animation = gameObject.AddComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>();
        SkinnedMeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html) renderer = gameObject.AddComponent<SkinnedMeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html)>();  
  
        // Build a rectangular mesh using four vertices and two triangles, and assign a material to the renderer
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        mesh.vertices = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] { new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 0, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 5, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 5, 0) };
        mesh.triangles = new int[] { 0, 1, 2, 1, 3, 2 };
        mesh.RecalculateNormals();
        renderer.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));  
  
        // Create a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) and bind pose for two bones
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[] bones = new Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[2];
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)[] bindPoses = new Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)[2];  
  
        // Create a bottom-left bone as a child of this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        bones[0] = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("BottomLeftBone").transform;
        bones[0].parent = transform;
        bones[0].localRotation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
        bones[0].localPosition = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        // Set the bind pose to the bone's inverse transformation matrix, relative to the root
        bindPoses[0] = bones[0].worldToLocalMatrix * transform.localToWorldMatrix;  
  
        // Create a top-right bone
        bones[1] = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("TopRightBone").transform;
        bones[1].parent = transform;
        bones[1].localRotation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
        bones[1].localPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 5, 0);
        bindPoses[1] = bones[1].worldToLocalMatrix * transform.localToWorldMatrix;  
  
        // Create an array that describes the number of bone weights per vertex
        // The array assigns 1 bone weight to vertex 0, 2 bone weights to vertex 1, and so on.
        byte[] bonesPerVertex = new byte[4] { 1, 2, 2, 1 };  
  
        // Create a array with one BoneWeight1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) struct for each of the 6 bone weights
        BoneWeight1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html)[] weights = new BoneWeight1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html)[6];  
  
        // Assign the bottom-left bone to vertex 0 (the bottom-left corner)
        weights[0].boneIndex = 0;
        weights[0].weight = 1;  
  
        // Assign both bones to vertex 1 (the bottom-right corner)
        weights[1].boneIndex = 0;
        weights[1].weight = 0.5f;  
  
        weights[2].boneIndex = 1;
        weights[2].weight = 0.5f;  
  
        // Assign both bones to vertex 2 (the top-left corner)
        weights[3].boneIndex = 0;
        weights[3].weight = 0.5f;  
  
        weights[4].boneIndex = 1;
        weights[4].weight = 0.5f;  
  
        // Assign the top-right bone to vertex 3 (the top-right corner)
        weights[5].boneIndex = 1;
        weights[5].weight = 1;  
  
        // Create NativeArray versions of the two arrays
        var bonesPerVertexArray = new NativeArray<byte>(bonesPerVertex, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        var weightsArray = new NativeArray<BoneWeight1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html)>(weights, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));  
  
        // Set the bone weights on the mesh
        mesh.SetBoneWeights(bonesPerVertexArray, weightsArray);
        bonesPerVertexArray.Dispose();
        weightsArray.Dispose();  
  
        // Assign the bind poses to the mesh
        mesh.bindposes = bindPoses;  
  
        // Assign the bones and the mesh to the renderer
        renderer.bones = bones;
        renderer.sharedMesh = mesh;  
  
        // Assign a simple back-and-forth animation to the bottom-left bone, and play the animation
        // Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) 0 moves directly with the bone
        // Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) 1 and 2 also move, but there's less movement because the vertices are also weighted to the top-right bone
        // Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) 3 doesn't move, because the top-right bone doesn't move
        AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve = new AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)();
        curve.keys = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[] { new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(0f, 0f, 0f, 0f), new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(1f, 3f, 0f, 0f), new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(2f, 0f, 0f, 0f) };
        AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip = new AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)();
        clip.legacy = true;
        clip.SetCurve("BottomLeftBone", typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)), "m_LocalPosition.z", curve);
        clip.wrapMode = WrapMode.Loop[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.Loop.html);
        animation.AddClip(clip, "test");
        animation.Play("test");  
  
    }
}
```

* * *
