#!/usr/bin/env python
"""
Test script to validate Django settings can be imported
This helps debug Heroku deployment issues
"""
import os
import sys
import django
from django.conf import settings

def test_settings():
    print("=== Heroku Settings Test ===")
    
    # Set the settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    
    try:
        # Configure Django
        django.setup()
        print("✅ Django setup successful")
        
        # Test database configuration
        print(f"Database engine: {settings.DATABASES['default']['ENGINE']}")
        
        # Test static files
        print(f"Static URL: {settings.STATIC_URL}")
        print(f"Static root: {settings.STATIC_ROOT}")
        
        # Test allowed hosts
        print(f"Allowed hosts: {settings.ALLOWED_HOSTS}")
        
        print("✅ All settings validated successfully")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_settings()
