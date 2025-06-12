* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).boneWeights
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
boneWeights; 
### Description
The [BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html) for each vertex in the Mesh, which represents 4 bones per vertex.
The size of this array is either [Mesh.vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexCount.html) or zero. The array is sorted by vertex index.  
  
Note that this property uses [BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html) structs, which represent exactly 4 bone weights per vertex. The newer [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) struct describes a single bone weight, and it can be used with the associated [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html) and [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html) APIs to describe up to 255 bone weights per vertex. It is preferable to use [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) and its associated APIs; they offer more flexibility, and might result in small performance benefits as Unity does not have to perform unnessary conversion operations.  
  
Additional resources: [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html), [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html), [Mesh.GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html), [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
```
using UnityEngine;  
  
public class SkinnedMeshExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html){
    void Start(){
        gameObject.AddComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>();
        gameObject.AddComponent<SkinnedMeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html)>();
        SkinnedMeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html) rend = GetComponent<SkinnedMeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html)>();
        Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim = GetComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>();  
  
        // Build basic mesh
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        mesh.vertices = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] {new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-1, 0, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 0, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-1, 5, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 5, 0)};
        mesh.uv = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] {new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 1)};
        mesh.triangles = new int[] { 0, 3, 1, 0, 2, 3 };
        mesh.RecalculateNormals();  
  
        // Assign mesh to mesh filter & renderer
        rend.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Diffuse"));  
  
        // Assign bone weights to mesh
        // We use 2 bones. One for the lower vertices, one for the upper vertices.
        BoneWeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html)[] weights = new BoneWeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html)[4];  
  
        weights[0].boneIndex0 = 0;
        weights[0].weight0 = 1;  
  
        weights[1].boneIndex0 = 0;
        weights[1].weight0 = 1;  
  
        weights[2].boneIndex0 = 1;
        weights[2].weight0 = 1;  
  
        weights[3].boneIndex0 = 1;
        weights[3].weight0 = 1;  
  
        // A BoneWeights array (weights) was just created and the boneIndex and weight assigned.
        // The weights array will now be assigned to the boneWeights array in the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).
        mesh.boneWeights = weights;  
  
        // Create Bone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Bone.html) Transforms and Bind poses
        // One bone at the bottom and one at the top
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[] bones = new Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[2];
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)[] bindPoses = new Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)[2];  
  
        bones[0] = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Lower").transform;
        bones[0].parent = transform;
        // Set the position relative to the parent
        bones[0].localRotation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
        bones[0].localPosition = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);  
  
        // The bind pose is bone's inverse transformation matrix
        // In this case the matrix we also make this matrix relative to the root
        // So that we can move the root game object around freely
        bindPoses[0] = bones[0].worldToLocalMatrix * transform.localToWorldMatrix;  
  
        bones[1] = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Upper").transform;
        bones[1].parent = transform;
        // Set the position relative to the parent
        bones[1].localRotation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
        bones[1].localPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 5, 0);
        // The bind pose is bone's inverse transformation matrix
        // In this case the matrix we also make this matrix relative to the root
        // So that we can move the root game object around freely
        bindPoses[1] = bones[1].worldToLocalMatrix * transform.localToWorldMatrix;  
  
        // assign the bindPoses array to the bindposes array which is part of the mesh.
        mesh.bindposes = bindPoses;  
  
        // Assign bones and bind poses
        rend.bones = bones;
        rend.sharedMesh = mesh;  
  
        // Assign a simple waving animation to the bottom bone
        AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve = new AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)();
        curve.keys = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[] {new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(0, 0, 0, 0), new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(1, 3, 0, 0), new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(2, 0.0F, 0, 0)};  
  
        // Create the clip with the curve
        AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip = new AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)();
        clip.SetCurve("Lower", typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)), "m_LocalPosition.z", curve);
        clip.legacy = true;
        clip.wrapMode = WrapMode.Loop[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.Loop.html);  
  
        // Add and play the clip
        anim.AddClip(clip, "test");
        anim.Play("test");
    }
}

```

* * *
