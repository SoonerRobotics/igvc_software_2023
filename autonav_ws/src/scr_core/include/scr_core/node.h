#pragma once

#include "scr_msgs/msg/configuration_instruction.hpp"
#include "scr_msgs/srv/set_system_state.hpp"
#include "scr_msgs/srv/set_device_state.hpp"
#include "scr_msgs/msg/device_state.hpp"
#include "scr_msgs/msg/system_state.hpp"
#include "scr_msgs/msg/log.hpp"
#include "rclcpp/rclcpp.hpp"
#include "configuration.h"
#include "device_state.h"
#include "system_state.h"
#include <stdint.h>
#include <string.h>
#include "utils.h"
#include <map>

namespace SCR
{
	class Node : public rclcpp::Node
	{
	public:
		Node(std::string node_name);
		~Node();

		void setSystemState(SystemState state);
		void setDeviceState(DeviceState state);
		void setEStop(bool state);
		void setMobility(bool state);

		Configuration config;

		DeviceState getDeviceState();
		DeviceState getDeviceState(std::string device);
		scr_msgs::msg::SystemState getSystemState();

		int64_t getDeviceID();
		std::map<int64_t, DeviceState> getDeviceStates();

		void log(const std::string& message);

	protected:
		virtual void configure();
		virtual void transition(scr_msgs::msg::SystemState old, scr_msgs::msg::SystemState updated);

	private:
		void onSystemState(const scr_msgs::msg::SystemState::SharedPtr msg);
		void onDeviceState(const scr_msgs::msg::DeviceState::SharedPtr msg);

	private:
		rclcpp::Subscription<scr_msgs::msg::SystemState>::SharedPtr systemStateSubscriber;
		rclcpp::Subscription<scr_msgs::msg::DeviceState>::SharedPtr deviceStateSubscriber;
		rclcpp::Publisher<scr_msgs::msg::Log>::SharedPtr logPublisher;
		rclcpp::Client<scr_msgs::srv::SetSystemState>::SharedPtr systemStateClient;
		rclcpp::Client<scr_msgs::srv::SetDeviceState>::SharedPtr deviceStateClient;
		std::map<int64_t, DeviceState> deviceStates;
		scr_msgs::msg::SystemState state;

		int64_t id;
	};
}