* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html

# TextureImporterSettings
class in UnityEditor
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
Stores settings of a [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).
Additional resources: [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).
### Properties
Property | Description  
---|---  
[alphaIsTransparency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-alphaIsTransparency.html) | If the alpha channel of your texture represents transparency, enable this property to dilate the color channels of visible texels into fully transparent areas. This effectively adds padding around transparent areas that prevents filtering artifacts from forming on their edges. Unity does not support this property for HDR textures.This property makes the color data of invisible texels undefined. Disable this property to preserve invisible texels' original color data.  
[alphaSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-alphaSource.html) | Select how the alpha of the imported texture is generated.  
[alphaTestReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-alphaTestReferenceValue.html) | Returns or assigns the alpha test reference value.  
[aniso](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-aniso.html) | Anisotropic filtering level of the texture.  
[borderMipmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-borderMipmap.html) | Enable this to avoid colors seeping out to the edge of the lower Mip levels. Used for light cookies.  
[convertToNormalMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-convertToNormalMap.html) | Convert heightmap to normal map?  
[cubemapConvolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-cubemapConvolution.html) | Convolution mode.  
[fadeOut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-fadeOut.html) | Fade out mip levels to gray color?  
[filterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-filterMode.html) | Filtering mode of the texture.  
[flipbookColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-flipbookColumns.html) | The number of columns in the source image for a Texture2DArray or Texture3D.  
[flipbookRows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-flipbookRows.html) | The number of rows in the source image for a Texture2DArray or Texture3D.  
[flipGreenChannel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-flipGreenChannel.html) | Indicates whether to invert the green channel values of a normal map.  
[generateCubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-generateCubemap.html) | Cubemap generation mode.  
[heightmapScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-heightmapScale.html) | Amount of bumpyness in the heightmap.  
[ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-ignoreMipmapLimit.html) | Enable this flag for textures that should ignore mipmap limit settings.  
[ignorePngGamma](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-ignorePngGamma.html) | Ignore the Gamma attribute in PNG files. This property does not effect other file formats.  
[mipmapBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-mipmapBias.html) | Mipmap bias of the texture.  
[mipmapEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-mipmapEnabled.html) | Generate mipmaps for the texture?  
[mipmapFadeDistanceEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-mipmapFadeDistanceEnd.html) | Mip level where texture is faded out to gray completely.  
[mipmapFadeDistanceStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-mipmapFadeDistanceStart.html) | Mip level where texture begins to fade out to gray.  
[mipmapFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-mipmapFilter.html) | Mipmap filtering mode.  
[mipMapsPreserveCoverage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-mipMapsPreserveCoverage.html) | Enables or disables coverage-preserving alpha mipmapping.  
[normalMapFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-normalMapFilter.html) | Normal map filtering mode.  
[npotScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-npotScale.html) | Scaling mode for non power of two textures.  
[readable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-readable.html) | Is texture data readable from scripts.  
[singleChannelComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-singleChannelComponent.html) | Color or Alpha component Single Channel Textures uses.  
[spriteAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spriteAlignment.html) | Edge-relative alignment of the sprite graphic.  
[spriteBorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spriteBorder.html) | Border sizes of the generated sprites.  
[spriteExtrude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spriteExtrude.html) | The number of blank pixels to leave between the edge of the graphic and the mesh.  
[spriteGenerateFallbackPhysicsShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spriteGenerateFallbackPhysicsShape.html) | Generates a default physics shape for a Sprite if a physics shape has not been set by the user.  
[spriteMeshType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spriteMeshType.html) |  SpriteMeshType defines the type of Mesh that TextureImporter generates for a Sprite.  
[spriteMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spriteMode.html) | Sprite texture import mode.  
[spritePivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spritePivot.html) | Pivot point of the Sprite relative to its graphic's rectangle.  
[spritePixelsPerUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spritePixelsPerUnit.html) | The number of pixels in the sprite that correspond to one unit in world space.  
[spriteTessellationDetail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-spriteTessellationDetail.html) | The tessellation detail to be used for generating the mesh for the associated sprite if the SpriteMode is set to Single. For Multiple sprites, use the SpriteEditor to specify the value per sprite. Valid values are in the range [0-1], with higher values generating a tighter mesh. A default of -1 will allow Unity to determine the value automatically.  
[sRGBTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-sRGBTexture.html) | Whether this texture stores data in sRGB (also called gamma) color space.  
[streamingMipmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-streamingMipmaps.html) | Enable mipmap streaming for this texture.  
[streamingMipmapsPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-streamingMipmapsPriority.html) | Relative priority for this texture when reducing memory size in order to hit the memory budget.  
[swizzleA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-swizzleA.html) | Specifies the source for the texture's alpha color channel data.  
[swizzleB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-swizzleB.html) | Specifies the source for the texture's blue color channel data.  
[swizzleG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-swizzleG.html) | Specifies the source for the texture's green color channel data.  
[swizzleR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-swizzleR.html) | Specifies the source for the texture's red color channel data.  
[textureShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-textureShape.html) | The shape of the imported texture.  
[textureType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-textureType.html) | Which type of texture are we dealing with here.  
[vtOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-vtOnly.html) | Enable if the texture is purposed solely for use with a Texture Stack for Virtual Texturing.  
[wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-wrapMode.html) | Texture coordinate wrapping mode.  
[wrapModeU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-wrapModeU.html) | Texture U coordinate wrapping mode.  
[wrapModeV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-wrapModeV.html) | Texture V coordinate wrapping mode.  
[wrapModeW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-wrapModeW.html) | Texture W coordinate wrapping mode for Texture3D.  
### Public Methods
Method | Description  
---|---  
[ApplyTextureType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.ApplyTextureType.html) | Configure parameters to import a texture for a purpose of type, as described here.  
[CopyTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.CopyTo.html) | Copy parameters into another TextureImporterSettings object.  
### Static Methods
Method | Description  
---|---  
[Equal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.Equal.html) | Test texture importer settings for equality.  
* * *
