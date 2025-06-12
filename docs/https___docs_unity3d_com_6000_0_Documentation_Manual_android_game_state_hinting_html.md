* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-game-state-hinting.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Optimization for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimization.html)
  * Game state hinting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-application-startup.html)
Optimize application startup times
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-for-user-preferences.html)
Optimize for user preferences
# Game state hinting
Android’s [game state](https://developer.android.com/reference/android/app/GameState) feature indicates to the operating system whether your application is in a loading state and also whether Android can interrupt the application. Depending on the state of the application, Android can perform certain optimizations. For example, if the application is in a loading state, the operating system can provide more resources to the application to help optimize the load process. However, whether the operating system does this depends on various other factors and settings, so you can’t guarantee that this will always happen.
## Requirements and compatibility
Android’s game state feature requires Android version 13.
## Game state hinting in Unity
Unity provides game state hinting in two ways.
  * Automated game state hinting (default behavior).
  * Manual game state hinting using [AndroidGame.SetGameState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.SetGameState.html) method.


### Automated game state hinting
Unity Player automatically sets the following parameters to indicate the game state to the operating system:
  * Application loading state as `isLoading` parameter. This parameter is set to true during initial loading, when loading a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), loading asset packs, or when sending a web request.
  * Current scene index or the type of the currently loaded content as `label` parameter.
  * Current quality level as `quality` parameter.
  * Default game state mode [MODE_UNKNOWN](https://developer.android.com/reference/android/app/GameState#MODE_UNKNOWN) as `mode` parameter. The default value is changed to [MODE_CONTENT](https://developer.android.com/reference/android/app/GameState#MODE_CONTENT) when a full-screen video or a full-screen ad is displayed.


You can use the [AndroidGame.Automatic.SetGameState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.Automatic.SetGameState.html) method to override the default [MODE_UNKNOWN](https://developer.android.com/reference/android/app/GameState#MODE_UNKNOWN) mode with the value based on the actual state of your game. 
### Manual game state hinting
You can use [AndroidGame.SetGameState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.SetGameState.html) method to indicate the current game state of your application to Android. It’s best practice to call this method when your application transitions to or from a loading state to make sure the operating system is aware of the state of your application.
**Note** : Automated game state hinting is disabled if you call [AndroidGame.SetGameState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.SetGameState.html) method.
## Additional resources
  * [Game state parameters](https://developer.android.com/reference/android/app/GameState#GameState\(boolean,%20int,%20int,%20int\))


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-application-startup.html)
Optimize application startup times
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-for-user-preferences.html)
Optimize for user preferences
