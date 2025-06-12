* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Searching.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * Search in the Editor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UndoWindow.html)
Undo
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomizingYourWorkspace.html)
Customizing your workspace
# Search in the Editor
There are two types of search functionality available:
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html) (formerly QuickSearch)- more advanced search features including performing actions on the results. To open choose **Edit** > **Search All** , or in **Preferences** [set the Search Engines](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html#search) to **Default**.
  * Legacy Search - the original search functionality for Unity, described below.


Legacy search functionality allows you to search the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view and Hierarchy window for **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), and the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) for assets.
Each search bar has the same basic workflow. To enter a search term, select the textbox and type a word or phrase. While you type, Unity automatically searches for those terms and provides the results.
Some search bars allow you to search by different criteria, such as name, type, or label. To select the criteria you want to search, select the magnifying glass icon on the bar to open the Search drop-down menu, and choose which criteria to use.
To clear your search and return your GameObject or Asset list view to normal, empty the search bar or select the small x icon in the search bar.
## Search for GameObjects in the Scene view and Hierarchy window
Both the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) and the Hierarchy window have a search bar that allows you to search for GameObjects by name or type. The Scene view and Hierarchy window represent the same information, and when you use one search bar, Unity automatically populates the other search bar with the same text.
A search term acts as a filter for the GameObjects in the Scene view and Hierarchy Window.
  * In the Scene view, GameObjects that match the search term appear in color. All other GameObjects appear in gray.
  * In the Hierarchy window, GameObjects that match the search term appear in alphabetical order. All the other GameObjects disappear from view.

![Scene and Hierarchy views with search filtering applied](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SearchingInEditor-Scene.png) Scene and Hierarchy views with search filtering applied
## Search for assets in the Project view
The Project window has a search bar that allows you to search for assets by name, type, or label. Select the magnifying glass in the search box to define which criteria to search by.
A search term acts as a filter for the assets in the Project window. Assets that match the search term appear in alphabetical order. Assets that do not match the search term do not appear in the results.
### Asset labels
A label is a short piece of text that you can use to group particular assets. To view the menu of existing labels, navigate to the Project window header and select the **Search by Label** button (the label icon). Select a label from the menu to search the project for any assets that have that label assigned to them.
To add a label to an asset, follow these steps:
  1. Open the asset in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** and find the preview panel at the bottom. This window might be minimized; if this is the case, click and drag the title bar upwards to expand it.
![The label icon found in the preview panel](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SearchingInEditor-Inspector.png) The label icon found in the preview panel
  2. To open the **label menu** , click the **label icon** shown on the bottom right of this panel.
  3. To add an existing label to the asset, select a label from this menu. Labels currently applied to the asset have a check mark next to them.
![Adding a new label to an asset](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SearchingInEditor-Labels.png) Adding a new label to an asset
  4. To add a new label, you first need to create one. Type your new label name into the text box shown at the top of the menu and press either Space or Enter. This creates a label which you can then add to any asset, and use to search in the Project window. Assets can have as many labels as desired and belong to several different label groups at once.


To remove a label from an asset, open the label menu and select it to remove the tick icon.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UndoWindow.html)
Undo
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomizingYourWorkspace.html)
Customizing your workspace
