* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * [Creating AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
  * Organizing assets into AssetBundles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
Creating AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html)
Build assets into an AssetBundle
# Organizing assets into AssetBundles
When you create an AssetBundle, there are some [limitations](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html#assetbundle-limitations) and organizational strategies to be aware of.
You can organize your assets in the following ways:
  * **[By function](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html#organize-assets-by-function)** : Organize assets based on functional portions of your project. Typical categories might include user interface, characters, environments, and other elements frequently used throughout your application.
  * **[By type](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html#organize-assets-by-type)** : Type Grouping focuses on bundling assets of the same type together, such as audio tracks or localization files.
  * **[By use at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html#organize-assets-by-use-at-runtime)** : Group assets that are loaded and used simultaneously. This strategy is often used for level-based projects.


You can mix these strategies within your project to get the best efficiency for your application. For example, you might group UI elements for different platforms into one AssetBundle, but group its interactive content by level or **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
## AssetBundle limitations
There are some limitations to what assets you can put in an AssetBundle, and how you set them up. The following table contains limitations of AssetBundles:
**Limitation** | **Description**  
---|---  
**File types** | 
  * You can’t combine scenes and assets into one AssetBundle. You must store scenes in a separate AssetBundle to one which contains assets.
  * You can’t include script assets in AssetBundles.
  * You can’t include files in the StreamingAssets folder.
  * You can’t assign assets or scenes to more than one AssetBundle.

  
**Naming** | The name of the AssetBundle must differ from the output folder.  
**Platform support** | AssetBundles can only be loaded on the specific platform you build them for. The Editor can load any AssetBundle, regardless of the platform defined in the [Build Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile), but some assets might not load properly if they use a platform-specific format not supported by the operating system the Editor is installed on.  
## General organization tips
Whatever organizational approach you take, it’s best practice to follow these general guidelines:
  * Separate frequently updated objects from rarely changed ones into different AssetBundles.
  * Create separate AssetBundles for sets of objects unlikely to be loaded at the same time, such as standard and high definition assets. You can use [AssetBundle variants](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Preparing.html#assetbundle-variants) to organize this.
  * Group objects together that are commonly loaded together. For example, a model, its textures, and its animations.
  * Split an AssetBundle if less than half of its content is ever loaded at the same time.
  * Combine small AssetBundles if the content is frequently loaded simultaneously.
  * If multiple objects in one AssetBundle depend on a single asset from another AssetBundle, consider moving the dependency to its own AssetBundle. Similarly, if several AssetBundles reference the same group of assets, consider putting the dependencies into a shared AssetBundle.


## AssetBundle variants
You can use AssetBundle variants to create multiple versions of an AssetBundle optimized for different situations or configurations, such as varying graphics settings. For example, you can create variants for low, medium, and high resolution textures to support devices with varying performance capabilities or user-selected graphics settings.
When using AssetBundle variants, Unity allows you to specify a variant name for each AssetBundle. The combination of AssetBundle name and variant name uniquely identifies each AssetBundle variant. For example, an AssetBundle named `environment` might have variants named `lowQuality`, `mediumQuality`, and `highQuality`.
The asset file names within the AssetBundles must match, but the content can differ based on the purpose of the variant.
You can create a variant in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), using the variant dropdown next to the AssetBundle, or use [`AssetImporter.assetBundleVariant`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleVariant.html).
## Organize assets by function
Organizing assets by how they functionally work together is useful in situations like the following:
  * Bundling all the textures and layout data for a UI screen.
  * Bundling all the models and animations for a character or set of characters.
  * Bundling the textures and models for pieces of the scenery shared across multiple levels.


This approach is ideal for downloadable content (DLC), because you can make small changes to your project without having to distribute large amounts of unchanged assets to your users. However, when using this approach, you must be familiar with where and when each asset is used in the project.
## Organize assets by type
You can organize assets of similar type, such as audio tracks or language localization files, into a single AssetBundle, which can be useful in AssetBundles that change rarely. 
Grouping AssetBundles this way can result in fewer AssetBundles changing and requiring distribution when creating an incremental build. However, more AssetBundles might need to be downloaded and loaded to assemble all dependent objects together at runtime.
## Organize assets by use at runtime
You can group together assets that Unity loads and uses at the same time, which is useful if you want to load AssetBundles based on scenes. For example, you can use this approach for a level-based game where each level contains unique assets, and an AssetBundle contains all a scene’s dependencies.
However, this approach means that an asset in one AssetBundle can only be used at the same time that the rest of the assets are going to be used, or it increases load times. 
**Important** An AssetBundle containing a scene automatically includes all assets referenced in that scene unless they are explicitly assigned to a separate AssetBundle. This might lead to duplicated assets if any other scenes use the referenced assets in other AssetBundles.
## Asset duplication
Unity uses the [Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html) to discover all dependencies of an object when it’s built into an AssetBundle. Unity uses this dependency information to determine the set of objects to include in an AssetBundle. 
AssetBundle assignment happens at the asset level. Objects in an asset explicitly assigned to an AssetBundle are included only in that specific AssetBundle. Depending on the [`BuildPipeline.BuildAssetBundles`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) method used, an asset is explicitly assigned either by setting its [`AssetImporter.assetBundleName`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.assetBundleName.html) property to a non-empty string, or by listing it in [`AssetBundleBuild.assetNames`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.assetNames.html).
Any object that’s part of an asset not explicitly assigned in an AssetBundle is included in each AssetBundle that contains any objects that reference it.
For example, if two objects are assigned to separate AssetBundles but share a reference to the same dependency object, Unity duplicates the dependency object into both AssetBundles. These duplicated dependencies are also instanced, meaning the two copies are treated as distinct objects with unique identifiers. This increases the overall size of the application’s AssetBundles and results in two separate copies of the object being loaded into memory if both parent AssetBundles are loaded.
### Avoiding asset duplication
You can use the following approaches to avoid asset duplication:
  * **Remove shared dependencies:** Make sure objects in different AssetBundles don’t share dependencies. Place any objects with shared dependenices into the same AssetBundle. **Note:** This approach doesn’t work in projects with many shared dependencies, because it creates large AssetBundles which must be rebuilt and downloaded frequently.
  * **Control asset loading** : Segment AssetBundles so that AssetBundles that share a dependency aren’t loaded at the same time. This approach works well for projects such as level-based games. However, duplicated objects increase the build time and sizes of AssetBundles.
  * **Build dependency assets into individual AssetBundles** : This approach removes the risk of duplicated assets, but also introduces complexity. The application must track dependencies between AssetBundles, and ensures that the right AssetBundles are loaded before calling any `AssetBundle.LoadAsset` APIs.


Object dependencies are tracked via the `AssetDatabase` API, in the `UnityEditor`namespace. This API is only available in the Unity Editor and not at runtime. Use [`AssetDatabase.GetDependencies`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetDependencies.html) to get the immediate dependencies of a specific object or asset. Dependencies might have their own dependencies so this can be a recursive calculation. 
Assets can be assigned to AssetBundles explicitly by passing arrays of `AssetBundleBuild` structures to `BuildPipeline.BuildAssetBundles`, or by querying the assignment using the `AssetImporter` API. You can also create an Editor script to ensure that all direct or **indirect dependencies** An **indirect** , or transitive dependency occurs when your project requests a package which itself “depends on” another package. For example, if your project depends on the `alembic@1.0.7` package which in turn depends on the `timeline@1.0.0` package, then your project has an direct dependency on Alembic and an indirect dependency on Timeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Indirectdependency) of an AssetBundle are assigned to AssetBundles, or to verify that no two AssetBundles share dependencies that haven’t been explicitly assigned.
**Note** : If you use the [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html) package, you can use the **Addressables Analyze** tool to discover duplicated assets.
## Additional resources
  * [Managing assets with the Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html)
  * [Build assets into an AssetBundle](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
Creating AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Building.html)
Build assets into an AssetBundle
