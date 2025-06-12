* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-plugins.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [Device Simulator](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator.html)
  * Extending the device simulator


[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html)
Adding a device
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html)
The Hierarchy window
# Extending the device simulator
The Device Simulator supports plugins to extend its functionality and change the UI of the Control Panel in the Simulator view.
## Creating a plugin
To create a Device Simulator plugin, extend the [DeviceSimulatorPlugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceSimulation.DeviceSimulatorPlugin.html) class. 
To insert UI into the Device Simulator view, your plugin must:
  * Override the `title` property to return a non-empty string.
  * Override the `OnCreateUI` method to return a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) that contains the UI.


If your plugin doesn’t meet these conditions, the Device Simulator instantiates the plugin but doesn’t display its UI in the Simulator view.
The following example demonstrates how to create a plugin that overrides the title property and adds UI to the Simulator view.
```
public class TouchInfoPlugin : DeviceSimulatorPlugin
{
    public override string title => "Touch Info";
    private Label m_TouchCountLabel;
    private Label m_LastTouchEvent;
    private Button m_ResetCountButton;

    [SerializeField]
    private int m_TouchCount = 0;

    public override void OnCreate()
    {
        deviceSimulator.touchScreenInput += touchEvent =>
        {
            m_TouchCount += 1;
            UpdateTouchCounterText();
            m_LastTouchEvent.text = $"Last touch event: {touchEvent.phase.ToString()}";
        };
    }

    public override VisualElement OnCreateUI()
    {
        VisualElement root = new VisualElement();
        
        m_LastTouchEvent = new Label("Last touch event: None");
        
        m_TouchCountLabel = new Label();
        UpdateTouchCounterText();

        m_ResetCountButton = new Button {text = "Reset Count" };
        m_ResetCountButton.clicked += () =>
        {
            m_TouchCount = 0;
            UpdateTouchCounterText();
        };

        root.Add(m_LastTouchEvent);
        root.Add(m_TouchCountLabel);
        root.Add(m_ResetCountButton);
            
        return root;
    }

    private void UpdateTouchCounterText()
    {
        if (m_TouchCount > 0)
            m_TouchCountLabel.text = $"Touches recorded: {m_TouchCount}";
        else
            m_TouchCountLabel.text = "No taps recorded";
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html)
Adding a device
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html)
The Hierarchy window
