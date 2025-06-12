* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.html

# ParticleSystemVertexStream
enumeration
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
All possible Particle System vertex shader inputs.
### Properties
Property | Description  
---|---  
[Position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Position.html) | The position of each particle vertex, in world space.  
[Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Normal.html) | The vertex normal of each particle.  
[Tangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Tangent.html) | The tangent vector for each particle (for normal mapping).  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Color.html) | The color of each particle.  
[UV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.UV.html) | The first UV stream of each particle.  
[UV2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.UV2.html) | The second UV stream of each particle.  
[UV3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.UV3.html) | The third UV stream of each particle (only for meshes).  
[UV4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.UV4.html) | The fourth UV stream of each particle (only for meshes).  
[AnimBlend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.AnimBlend.html) | The amount to blend between animated texture frames, from 0 to 1.  
[AnimFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.AnimFrame.html) | The current animation frame index of each particle.  
[Center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Center.html) | The center position of the entire particle, in world space.  
[VertexID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.VertexID.html) | The vertex ID of each particle.  
[SizeX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.SizeX.html) | The X axis size of each particle.  
[SizeXY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.SizeXY.html) | The X and Y axis sizes of each particle.  
[SizeXYZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.SizeXYZ.html) | The 3D size of each particle.  
[Rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Rotation.html) | The Z axis rotation of each particle.  
[Rotation3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Rotation3D.html) | The 3D rotation of each particle.  
[RotationSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.RotationSpeed.html) | The Z axis rotational speed of each particle.  
[RotationSpeed3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.RotationSpeed3D.html) | The 3D rotational speed of each particle.  
[Velocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Velocity.html) | The velocity of each particle, in world space.  
[Speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Speed.html) | The speed of each particle, calculated by taking the magnitude of the velocity.  
[AgePercent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.AgePercent.html) | The normalized age of each particle, from 0 to 1.  
[InvStartLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.InvStartLifetime.html) | The reciprocal of the starting lifetime, in seconds (1.0f / startLifetime).  
[StableRandomX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.StableRandomX.html) | A random number for each particle, which remains constant during their lifetime.  
[StableRandomXY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.StableRandomXY.html) | Two random numbers for each particle, which remain constant during their lifetime.  
[StableRandomXYZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.StableRandomXYZ.html) | Three random numbers for each particle, which remain constant during their lifetime.  
[StableRandomXYZW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.StableRandomXYZW.html) | Four random numbers for each particle, which remain constant during their lifetime.  
[VaryingRandomX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.VaryingRandomX.html) | A random number for each particle, which changes during their lifetime.  
[VaryingRandomXY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.VaryingRandomXY.html) | Two random numbers for each particle, which change during their lifetime.  
[VaryingRandomXYZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.VaryingRandomXYZ.html) | Three random numbers for each particle, which change during their lifetime.  
[VaryingRandomXYZW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.VaryingRandomXYZW.html) | Four random numbers for each particle, which change during their lifetime.  
[Custom1X](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom1X.html) | One custom value for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[Custom1XY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom1XY.html) | Two custom values for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[Custom1XYZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom1XYZ.html) | Three custom values for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[Custom1XYZW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom1XYZW.html) | Four custom values for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[Custom2X](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom2X.html) | One custom value for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[Custom2XY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom2XY.html) | Two custom values for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[Custom2XYZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom2XYZ.html) | Three custom values for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[Custom2XYZW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Custom2XYZW.html) | Four custom values for each particle, defined by the Custom Data Module, or ParticleSystem.SetCustomParticleData.  
[NoiseSumX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.NoiseSumX.html) | The accumulated X axis noise, over the lifetime of the particle.  
[NoiseSumXY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.NoiseSumXY.html) | The accumulated X and Y axis noise, over the lifetime of the particle.  
[NoiseSumXYZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.NoiseSumXYZ.html) | The accumulated 3D noise, over the lifetime of the particle.  
[NoiseImpulseX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.NoiseImpulseX.html) | The X axis noise on the current frame.  
[NoiseImpulseXY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.NoiseImpulseXY.html) | The X and Y axis noise on the current frame.  
[NoiseImpulseXYZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.NoiseImpulseXYZ.html) | The 3D noise on the current frame.  
[MeshIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.MeshIndex.html) | The index of the mesh used by the current particle.  
[ParticleIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.ParticleIndex.html) | The index of the current particle in the particle data array.  
[ColorPackedAsTwoFloats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.ColorPackedAsTwoFloats.html) | The color of each particle, packed in a special format to allow decoding on GPUs that do not support bit-packing operations.  
[MeshAxisOfRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.MeshAxisOfRotation.html) | The axis of rotation used by mesh particles when not using 3D rotation.  
[NextTrailCenter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.NextTrailCenter.html) | The center of the next trail position, connected to the current position.  
[PreviousTrailCenter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.PreviousTrailCenter.html) | The center of the previous trail position, connected to the current position.  
[PercentageAlongTrail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.PercentageAlongTrail.html) | The percentage along the trail, in the range 0-1.  
[TrailWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.TrailWidth.html) | The width of the trail.  
* * *
