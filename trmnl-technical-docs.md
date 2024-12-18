# TRMNL Technical Documentation

## System Architecture Overview

TRMNL is an IoT platform consisting of four main components:
1. Device Hardware
2. Web Server
3. Plugin System
4. Firmware (OSS)

### Device Specifications

The TRMNL device features:
- ESP32-C3 microcontroller
- 1800-2500 mAh battery capacity
- 7.5" EPD (Electronic Paper Display) screen
- 800x480 pixel resolution
- Injection-molded ABS soft touch plastic housing
- User-serviceable design supporting firmware modification

### Web Server Architecture

The server provides:
- Native plugin directory hosting
- API endpoint management
- Custom plugin templating engine
- Device authentication and management
- Image generation and serving

### Plugin System

Two types of plugins are supported:

1. Native Plugins
   - Accessed via GET /webhook and OAuth
   - Pre-built functionality
   - Managed by TRMNL

2. Custom Plugins
   - Customer-managed
   - Supports webhook (POST) and polling (GET) methods
   - Templating engine for customization

### Security and Privacy Model

TRMNL implements a "device-initiated" security model:

- Devices initiate all communication with the server
- No direct server-to-device connections
- Minimal data collection:
  - API key
  - Device MAC address
  - Firmware version
  - Battery voltage
  - WiFi signal strength
- No collection of:
  - IP addresses
  - WiFi configuration
  - Location data
  - User identity information

### Communication Flow

1. Device Wake Cycle:
   ```
   Device -> Server (GET /api/display)
   Server -> Device (Response with bitmap image + timing)
   Device -> Sleep state
   ```

2. Server Response Format:
   - Single-use 1-bit bitmap image
   - Next refresh timing instructions
   - Firmware update flags (if applicable)
   - Device reset instructions (if applicable)

### Content Management

- Display Priority:
  - Managed through Playlists interface
  - Most recent content takes precedence
  - Configurable refresh intervals

- Storage Policy:
  - Only most recent screen per plugin stored
  - Previous content automatically replaced
  - Minimizes storage costs
  - Enhances privacy protection

### Developer Features

- Open firmware modification
- API key access
- Developer add-on available (one-time fee)
- Terms of Service explicitly permit hardware modification

### Binary Management

- Firmware updates delivered via OTA
- Binary storage in S3
- Public access to firmware binaries
- Automatic update detection and deployment

### Configuration Management

Users can configure:
- Display refresh intervals (n minutes)
- Device settings via Devices > Edit interface
- WiFi credentials (stored only on device)
- Plugin preferences and priorities

### Privacy Considerations

1. Data Minimization:
   - Only essential device data collected
   - No persistent content storage
   - No network configuration storage

2. User Control:
   - Device reset capability
   - Ownership transfer support
   - Data destruction options

3. Transparency:
   - Open source firmware
   - Public binary access
   - User-serviceable hardware