def  send_motor_command(rpm: float, motor_id: int = 0) -> tuple[int,float]:
    """send a speed command to a specific motor with safety checks"""
    if rpm>1000:
        raise ValueError(f"safety limit exceed: {rpm} RPM is too high")
    return (motor_id,rpm)
commands_to_test = [500,1200]
for cmd in commands_to_test:
    try:
        m_id, speed= send_motor_command(cmd, motor_id=1)
        print(f"SUCCESS: MOTOR {m_id} set to {speed} rpm")
    except ValueError as e:
        print(f"Critical alert: {e}")
