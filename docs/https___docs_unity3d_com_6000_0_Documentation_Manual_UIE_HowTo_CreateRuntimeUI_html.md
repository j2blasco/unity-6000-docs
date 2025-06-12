* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateRuntimeUI.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-examples.html)
  * Create a list view runtime UI


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-list-view-complex.html)
Create a complex list view
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-wrap-content-inside-scrollview.html)
Wrap content inside a scroll view
# Create a list view runtime UI
**Version** : 2022.3+
This example demonstrates how to create a list view runtime UI. This example uses the UXML and USS files directly to create the structure and style of the UI. If You’re new to UI Toolkit and want to use UI Builder to create the UI, refer to [Create an example UI with UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-getting-started.html).
## Example overview
This example creates a simple character selection screen. When you click the name of a character from a list on the left, the detail of the character appears on the right.
![Final view of the runtime UI](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-runtimeUI-final.png) Final view of the runtime UI
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/create-listview-runtime-ui).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [`ListView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html)
  * [`Label`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)
  * [`PanelSettings`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings.html)
  * [`UIDocument`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html)


## Create the main UI Document
Create the main view UI Document and a USS file to style the **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). Add two visual elements as containers in the UI Document: one that contains the list of character names and another that contains the selected character’s details.
![The UI layout setup for the main view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-runtimeUI-finalMainView.png) The UI layout setup for the main view
  1. Create a project in Unity with any template.
  2. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `UI` to store all the UI Document and Style Sheet files.
  3. In the `UI` folder, create a UI Document named `MainView.uxml` with the following content:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" editor-extension-mode="False">
    <Style src="MainView.uss" />
    <ui:VisualElement name="background">
        <ui:VisualElement name="main-container">
            <ui:ListView focusable="true" name="character-list" />
            <ui:VisualElement name="right-container">
                <ui:VisualElement name="details-container">
                    <ui:VisualElement name="details">
                        <ui:VisualElement name="character-portrait" />
                    </ui:VisualElement>
                    <ui:Label text="Label" name="character-name" />
                    <ui:Label text="Label" display-tooltip-when-elided="true" name="character-class" />
                </ui:VisualElement>
            </ui:VisualElement>
        </ui:VisualElement>
    </ui:VisualElement>
</ui:UXML>

```

  4. In the `UI` folder, create a USS style sheet named `MainView.uss` with the following content:

```
#background {
    flex-grow: 1;
    align-items: center;
    justify-content: center;
    background-color: rgb(115, 37, 38);
}

#main-container {
    flex-direction: row;
    height: 350px;
}

#character-list {
    width: 230px;
    border-color: rgb(49, 26, 17);
    border-width: 4px;
    background-color: rgb(110, 57, 37);
    border-radius: 15px;
    margin-right: 6px;
}

#character-name {
    -unity-font-style: bold;
    font-size: 18px;
}

#character-class {
    margin-top: 2px;
    margin-bottom: 8px;
    padding-top: 0;
    padding-bottom: 0;
}

#right-container {
    justify-content: space-between; 
    align-items: flex-end;
}

#details-container {
    align-items: center; 
    background-color: rgb(170, 89, 57); 
    border-width: 4px; 
    border-color: rgb(49, 26, 17);
    border-radius: 15px;
    width: 252px; 
    justify-content: center; 
    padding: 8px;
    height: 163px;
}

#details {
    border-color: rgb(49, 26, 17); 
    border-width: 2px; 
    height: 120px; 
    width: 120px; 
    border-radius: 13px; 
    padding: 4px;
    background-color: rgb(255, 133, 84);
}

#character-portrait {
    flex-grow: 1; 
    -unity-background-scale-mode: scale-to-fit;
}

.unity-collection-view__item {
    justify-content: center;
}

```

## Create a list entry UI Document
Create a UI Document and a Style Sheet for the individual entries in the list. The character list entry consists of a colored background frame and the character’s name.
![List entry that shows a characters name](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie-howto-runtimeUI-listEntryFinal.png) List entry that shows a character’s name
  1. In the `UI` folder, create a UI Document named `ListEntry.uxml` with the following content:
```
<ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" editor-extension-mode="False">
<Style src="ListEntry.uss" />
<ui:VisualElement name="list-entry">
    <ui:Label text="Label" display-tooltip-when-elided="true" name="character-name" />
</ui:VisualElement>
</ui:UXML>

```

  2. In the `UI` folder, create a Style Sheet file named `ListEntry.uss` with the following content:

```
#list-entry {
    height: 41px;
    align-items: flex-start;
    justify-content: center;
    padding-left: 10px;
    background-color: rgb(170, 89, 57);
    border-color: rgb(49, 26, 17);
    border-width: 2px;
    border-radius: 15px;
}

#character-name {
    -unity-font-style: bold;
    font-size: 18px;
    color: rgb(49, 26, 17);
}

```

## Create sample data to display
Create sample data to fill the character list in the UI. For the character list, create a class that holds a character name, class, and a portrait image.
  1. In the Asset folder, create a folder named `Scripts` to store your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
  2. In the `Scripts` folder, create a C# script named `CharacterData.cs` with the following content:
```
using UnityEngine;
    
public enum ECharacterClass
{
    Knight, Ranger, Wizard
}
    
[CreateAssetMenu]
public class CharacterData : ScriptableObject
{
    public string CharacterName;
    public ECharacterClass Class;
    public Sprite PortraitImage;
}

```

This creates a **Character Data** item in the **Assets** > **Create** menu.
  3. In the Assets folder, create a folder named `Resources`.
  4. In the `Resources` folder, create a folder named `Characters` to store all your sample character data.
  5. In the `Characters` folder, right-click and select **Create** > **Character Data** to create an instance of the `ScriptableObject`.
  6. Create more `CharacterData` instances and fill them with placeholder data.


## Set up the scene
Create a UIDocument **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the SampleScene and add the UI Document as the source asset.
  1. In the SampleScene, select **GameObject** > **UI Toolkit** > **UI Document**.
  2. Select the **UIDocument** GameObject in the Hierarchy window.
  3. Drag **MainView.uxml** from your Project window to the **Source Asset** field of the UI Document component in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. This references the source asset to the UXML file.


## Create controllers for the list entry and the main view
Create two C# scripts with the following classes:
  * A `CharacterListEntryController` class to display the data of a character instance in the UI of the list entry. It needs to access the label for the character name and set it to display the name of the given character instance.
  * A `CharacterListController` class for the character list in the main view, and a `MonoBehaviour` script that instantiates and assigns it to the **visual tree** An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree).


**Note** : The `CharacterListEntryController` class isn’t a `MonoBehaviour`. Since the visual elements in UI Toolkit aren’t GameObjects, you can’t attach components to them. Instead, you attach the class to the `userData` property in the `CharacterListController` class.
  1. In the `Scripts` folder, create a C# script named `CharacterListEntryController.cs` with the following contents:
```
using UnityEngine.UIElements;
    
public class CharacterListEntryController
{
    Label m_NameLabel;
    
    // This function retrieves a reference to the 
    // character name label inside the UI element.
    public void SetVisualElement(VisualElement visualElement)
    {
        m_NameLabel = visualElement.Q<Label>("character-name");
    }
    
    // This function receives the character whose name this list 
    // element is supposed to display. Since the elements list 
    // in a `ListView` are pooled and reused, it's necessary to 
    // have a `Set` function to change which character's data to display.
    public void SetCharacterData(CharacterData characterData)
    {
        m_NameLabel.text = characterData.CharacterName;
    }
}

```

  2. In the `Scripts` folder, create a C# script named `CharacterListController.cs` with the following content:
```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;
    
public class CharacterListController
{
    // UXML template for list entries
    VisualTreeAsset m_ListEntryTemplate;
    
    // UI element references
    ListView m_CharacterList;
    Label m_CharClassLabel;
    Label m_CharNameLabel;
    VisualElement m_CharPortrait;
    
    List<CharacterData> m_AllCharacters;
    
    public void InitializeCharacterList(VisualElement root, VisualTreeAsset listElementTemplate)
    {
        EnumerateAllCharacters();
    
        // Store a reference to the template for the list entries
        m_ListEntryTemplate = listElementTemplate;
    
        // Store a reference to the character list element
        m_CharacterList = root.Q<ListView>("character-list");
    
        // Store references to the selected character info elements
        m_CharClassLabel = root.Q<Label>("character-class");
        m_CharNameLabel = root.Q<Label>("character-name");
        m_CharPortrait = root.Q<VisualElement>("character-portrait");
    
        FillCharacterList();
    
        // Register to get a callback when an item is selected
        m_CharacterList.selectionChanged += OnCharacterSelected;
    }
    
    void EnumerateAllCharacters()
    {
        m_AllCharacters = new List<CharacterData>();
        m_AllCharacters.AddRange(Resources.LoadAll<CharacterData>("Characters"));
    }
    
    void FillCharacterList()
    {
        // Set up a make item function for a list entry
        m_CharacterList.makeItem = () =>
        {
            // Instantiate the UXML template for the entry
            var newListEntry = m_ListEntryTemplate.Instantiate();
    
            // Instantiate a controller for the data
            var newListEntryLogic = new CharacterListEntryController();
    
            // Assign the controller script to the visual element
            newListEntry.userData = newListEntryLogic;
    
            // Initialize the controller script
            newListEntryLogic.SetVisualElement(newListEntry);
    
            // Return the root of the instantiated visual tree
            return newListEntry;
        };
    
        // Set up bind function for a specific list entry
        m_CharacterList.bindItem = (item, index) =>
        {
            (item.userData as CharacterListEntryController)?.SetCharacterData(m_AllCharacters[index]);
        };
    
        // Set a fixed item height matching the height of the item provided in makeItem. 
        // For dynamic height, see the virtualizationMethod property.
        m_CharacterList.fixedItemHeight = 45;
    
        // Set the actual item's source list/array
        m_CharacterList.itemsSource = m_AllCharacters;
    }
    
    void OnCharacterSelected(IEnumerable<object> selectedItems)
    {
        // Get the currently selected item directly from the ListView
        var selectedCharacter = m_CharacterList.selectedItem as CharacterData;
    
        // Handle none-selection (Escape to deselect everything)
        if (selectedCharacter == null)
        {
            // Clear
            m_CharClassLabel.text = "";
            m_CharNameLabel.text = "";
            m_CharPortrait.style.backgroundImage = null;
    
            return;
        }
    
        // Fill in character details
        m_CharClassLabel.text = selectedCharacter.Class.ToString();
        m_CharNameLabel.text = selectedCharacter.CharacterName;
        m_CharPortrait.style.backgroundImage = new StyleBackground(selectedCharacter.PortraitImage);
    }
}

```



## Attach the controller script to the main view
The `CharacterListController` isn’t a `MonoBehaviour`, so you can’t directly attach it to a GameObject. To overcome this, create a `MonoBehaviour` script and attach it to the same GameObject as the UIDocument. In this script, you don’t need to instantiate the `MainView.uxml` as it’s already instantiated by the UIDocument component. Instead, access the UIDocument component to get a reference of the already instantiated visual tree. Then, create an instance of the `CharacterListController` and pass in the root element of the visual tree and the UXML template used for the individual list elements.
**Note** : When the UI reloads, any associated `MonoBehaviour` components on the same GameObject that contain the UIDocument component are disabled before the reload, and then re-enabled after the reload. Therefore, you must place your UI-related code within the `OnEnable` and `OnDisable` methods of this `MonoBehaviour`. For more information, refer to [Lifecycle of UI Document components](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-ui-document-component.html#lifecycle-of-ui-document-components).
  1. In the `Scripts` folder, create a C# script named `MainView.cs` with the following content:
```
using UnityEngine;
using UnityEngine.UIElements;
    
public class MainView : MonoBehaviour
{
    [SerializeField]
    VisualTreeAsset m_ListEntryTemplate;
    
    void OnEnable()
    {
        // The UXML is already instantiated by the UIDocument component
        var uiDocument = GetComponent<UIDocument>();
    
        // Initialize the character list controller
        var characterListController = new CharacterListController();
        characterListController.InitializeCharacterList(uiDocument.rootVisualElement, m_ListEntryTemplate);
    }
}

```

  2. In the SampleScene, select **UIDocument**.
  3. Drag `MainView.cs` to **Add Component** in the Inspector window.
  4. Drag **ListEntry.uxml** to the **ListEntry Template** field.
  5. Enter Play mode to see your UI displayed in the game view.


## Additional resource
  * [UXML element ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html)
  * [Get started with runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-runtime-ui.html)
  * [Render UI in the Game view](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-render-runtime-ui.html)
  * [The Panel Settings asset](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html)
  * [Runtime event system](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-list-view-complex.html)
Create a complex list view
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-wrap-content-inside-scrollview.html)
Wrap content inside a scroll view
