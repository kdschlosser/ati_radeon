import ati_radeon

for adapter in ati_radeon.adapters:
    print('id', adapter.id)
    print('name', adapter.name)
    print('index', adapter.index)
    print('device_number', adapter.device_number)
    print('bus_number', adapter.bus_number)
    print('vendor_id', adapter.vendor_id)
    print('supports_edid_management', adapter.supports_edid_management)
    print('is_overdrive_enabled', adapter.is_overdrive_enabled)
    print('is_overdrive_supported', adapter.is_overdrive_supported)
    print('overdrive_version', adapter.overdrive_version)
    print('supported_aspects', adapter.supported_aspects)
    print('udid', adapter.udid)
    print('function_number', adapter.function_number)
    print('is_present', adapter.is_present)
    print('exists', adapter.exists)
    print('driver_path', adapter.driver_path)
    print('driver_path_ext', adapter.driver_path_ext)
    print('upnp_path', adapter.upnp_path)
    print('display_index', adapter.display_index)
    print('driver_index', adapter.driver_index)
    print('screen_config_name', adapter.screen_config_name)
    print('asic_family_type', adapter.asic_family_type)
    print('can_change_speed', adapter.can_change_speed)
    print('speed', adapter.speed)
    print('default_speed', adapter.default_speed)
    print('is_gpu_accessable', adapter.is_gpu_accessable)
    print('is_power_control_supported', adapter.is_power_control_supported)
    print('bus_speed', adapter.bus_speed)
    print('bus_lanes', adapter.bus_lanes)
    print('max_bus_lanes', adapter.bus_lanes.max)
    print()
    print('power_control')
    power_control = adapter.power_control
    print('    value', power_control)
    print('    min', power_control.min)
    print('    max', power_control.max)
    print('    step', power_control.step)
    print('    default', power_control.default)
    print()
    print('temperatures')
    temperatures = adapter.temperatures
    for temperature in temperatures:
        print('   ', temperature)

    print()
    print('fan_speeds')
    for fan_speed in adapter.fan_speeds:
        print('    speed', fan_speed, fan_speed.unit_of_measure)
        print('    min', fan_speed.min, fan_speed.unit_of_measure)
        print('    max', fan_speed.max, fan_speed.unit_of_measure)
        print('    automatic', fan_speed.automatic)
        print()

    print()
    print('firmware')
    firmware = adapter.firmware
    print('    date', firmware.date)
    print('    part_number', firmware.part_number)
    print('    version', firmware.version)

    print()
    print('core')
    core = adapter.core
    voltages = core.voltages
    clocks = core.clocks
    actual_clock = clocks.actual
    actual_voltage = voltages.actual
    load = core.load
    print('    actual clock', actual_clock, actual_clock.unit_of_measure)
    print('    actual voltage', actual_voltage, actual_voltage.unit_of_measure)
    print('    load', load, load.unit_of_measure)
    print()
    print('    clocks')
    for clock in clocks:
        print('        clock', clock, clock.unit_of_measure)
        print('        step', clock.step, clock.unit_of_measure)
        print('        default', clock.default, clock.unit_of_measure)
        print('        min', clock.min, clock.unit_of_measure)
        print('        max', clock.max, clock.unit_of_measure)
        print('        is_active', clock.is_active)
        print()

    print()
    print('    voltages')
    for voltage in voltages:
        print('        clock', voltage, voltage.unit_of_measure)
        print('        step', voltage.step, voltage.unit_of_measure)
        print('        default', voltage.default, voltage.unit_of_measure)
        print('        min', voltage.min, voltage.unit_of_measure)
        print('        max', voltage.max, voltage.unit_of_measure)
        print('        is_active', voltage.is_active)
        print()

    print()
    print('memory')
    memory = adapter.memory
    clocks = memory.clocks
    actual_clock = clocks.actual
    print('    size', memory.size)
    print('    type', memory.type)
    print('    bandwidth', memory.bandwidth)
    print('    actual_clock', actual_clock, actual_clock.unit_of_measure)

    print()
    print('    clocks')
    for clock in clocks:
        print('        clock', clock, clock.unit_of_measure)
        print('        step', clock.step, clock.unit_of_measure)
        print('        default', clock.default, clock.unit_of_measure)
        print('        min', clock.min, clock.unit_of_measure)
        print('        max', clock.max, clock.unit_of_measure)
        print('        is_active', clock.is_active)
        print()

    print()
    print('crossfire')
    crossfire = adapter.crossfire
    print('    is_prefered_adapter', crossfire.is_prefered_adapter)
    print('    is_combination_supported', crossfire.is_combination_supported)
    print('    state', crossfire.state)

    print()
    print('crossdisplay')
    crossdisplay = adapter.crossdisplay

    print()
    print('fps')
    fps = adapter.fps
    print('    is_supported', fps.is_supported)
    print('    version', fps.version)
    print('    type', fps.type)
    print('    is_enabled', fps.is_enabled)
    print('    value', fps.value)
    print('    maximum', fps.maximum)
    print('    minimum', fps.minimum)

    print()
    print('error_records')
    error_records = adapter.error_records
    for i, record in enumerate(error_records):
        print('    record_number', i)
        print('    severity', record.severity)
        print('    is_count_valid', record.is_count_valid)
        print('    count', record.count)
        print('    is_valid_location', record.is_location_valid)
        print('    cu', record.cu)
        print('    location_name', record.location_name)
        print('    timestamp', record.timestamp)
        print()

    print()
    print('connectors')
    connectors = adapter.connectors
    for connector in connectors:
        print('    index', connector.index)
        print('    active_connector', connector.active_connector)
        print('    mhl_ports', connector.mhl_ports)
        print('    child_ports', connector.child_ports)

        print()
        print('    supported_connections')
        for supported_connection in connector:
            print('        name', supported_connection.name)
            print('        supports_bitrate', supported_connection.supports_bitrate)
            print('        supports_number_of_lanes', supported_connection.supports_number_of_lanes)
            print('        supports_three_d_caps', supported_connection.supports_three_d_caps)
            print('        supports_output_bandwidth', supported_connection.supports_output_bandwidth)
            print('        supports_color_depth', supported_connection.supports_color_depth)
            print('        is_connected', supported_connection.is_connected)
            print('        bitrate', supported_connection.bitrate)
            print('        number_of_lanes', supported_connection.number_of_lanes)
            print('        three_d_caps', supported_connection.three_d_caps)
            print('        output_bandwidth', supported_connection.output_bandwidth)
            print('        color_depth', supported_connection.color_depth)
            print()

    print('\n\n')


