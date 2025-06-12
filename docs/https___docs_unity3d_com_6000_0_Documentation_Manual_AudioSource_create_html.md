* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
  * Set up an Audio Source component


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html)
Audio Source component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html)
Audio Mixer
# Set up an Audio Source component
Create an audio source to control how an audio clip plays, where it plays and how often. 
To create and configure an audio source: 
  1. [Import your audio files](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#import-your-audio-files).
  2. [Create an audio source](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#create-an-audio-source).
  3. [Assign an audio resource to your audio source](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#assign-an-audio-resource-to-your-audio-source).
  4. [Alter the settings of your audio source](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#alter-the-settings-of-your-audio-source).


## Import your audio files
To import your audio files into your Unity project, drag your audio file into your project. Unity imports these files as audio clips. For a list of the audio file formats Unity supports, refer to [Audio file compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html#audio-file-compatibility).
## Create an audio source
There are multiple ways to create an audio source. Use one of the following methods:
  * [Create an audio source from an audio file](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#create-an-audio-source-from-an-audio-file).
  * [Create an audio source from an existing GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#create-an-audio-source-from-an-existing-gameobject).
  * [Create an audio source from the menu](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#create-an-audio-source-from-the-menu).


### Create an audio source from an audio file
A quicker way to create an audio source is to click and drag an audio file from your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) into the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
As a result, Unity automatically creates a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with an **Audio Source** A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource) component, and assigns your audio file to its **Audio Clip** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) property. 
### Create an audio source from an existing GameObject
If you have a GameObject in your scene you want to add an audio source to: 
  1. Click on the GameObject.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, select **Add Component**.
  3. Select **Audio** > **Audio Source**.


As a result, Unity adds an **Audio Source** component to your GameObject. 
Another way to do this is to drag an audio file from your Project window onto the GameObject. Unity attaches the clip along with a new audio source if it doesn’t already have one. If the object already has an audio source the new clip will replace the one that the source currently uses.
### Create an audio source from the menu
To create a new audio source from the menu:
  1. In the **Hierarchy** tab, select the **Add (+)** button.
  2. Select **Audio** > **Audio Source**.


Unity adds a new GameObject that contains an **Audio Source** component to your scene. 
## Assign an audio resource to your audio source
If your audio source doesn’t have an audio resource assigned, you need to assign one. To do this: 
  1. Click on your GameObject that contains the **Audio Source** component. The Inspector window shows. 
  2. In the Inspector window, on the **Audio Source** component, locate the **Audio Resource** property.
  3. Then, do one of the following: 
  4. Drag an audio clip or audio random container from the Project window to the property.
  5. Click the small circle icon to the right of the property, then select a resource from the list.


## Alter the settings of your audio source
If you want to configure your audio source more to your liking, refer to [Audio Source component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html). 
## Additional resources
  * [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/Class-AudioSource.html)
  * [Introduction to the Audio Source component](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-overview.html)
  * [Audio Source component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html)
Audio Source component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html)
Audio Mixer
