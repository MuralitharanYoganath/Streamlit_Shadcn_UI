import streamlit as st
import streamlit_shadcn_ui as ui

ui.badges(badge_list=[("default", "default"), ("secondary", "secondary"), ("outline", "outline"), ("Hello", "destructive"), ("Murali", "destructive")], class_name="flex gap-2", key="badges1")