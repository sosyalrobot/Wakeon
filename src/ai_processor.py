"""
AI Processing using OpenAI API
"""

import logging
import config

# Try to import optional dependencies
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

logger = logging.getLogger(__name__)


class AIProcessor:
    """Handles AI processing using OpenAI API."""
    
    def __init__(self):
        """Initialize the AI processor."""
        logger.info("Initializing AI processor...")
        
        if not OPENAI_AVAILABLE:
            logger.warning("OpenAI not available. Using fallback responses.")
            self.use_fallback = True
            return
        
        try:
            # Configure OpenAI client
            if config.OPENAI_API_KEY == "your_api_key_here":
                logger.warning("OpenAI API key not configured. Using fallback responses.")
                self.use_fallback = True
            else:
                openai.api_key = config.OPENAI_API_KEY
                self.use_fallback = False
                logger.info("AI processor initialized with OpenAI")
                
        except Exception as e:
            logger.error(f"Failed to initialize AI processor: {e}")
            self.use_fallback = True
    
    def process_command(self, command):
        """
        Process a voice command with AI.
        
        Args:
            command (str): The voice command to process
            
        Returns:
            str: AI response or None if processing failed
        """
        logger.debug(f"Processing command: {command}")
        
        if self.use_fallback:
            return self._fallback_response(command)
        
        try:
            # Create chat completion
            response = openai.ChatCompletion.create(
                model=config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": command}
                ],
                max_tokens=config.OPENAI_MAX_TOKENS,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content.strip()
            logger.info(f"AI Response: {ai_response}")
            return ai_response
            
        except openai.error.AuthenticationError:
            logger.error("OpenAI authentication failed. Check your API key.")
            return "I'm sorry, I'm having trouble connecting to my AI service. Please check your API key."
            
        except openai.error.RateLimitError:
            logger.error("OpenAI rate limit exceeded.")
            return "I'm sorry, I'm receiving too many requests right now. Please try again later."
            
        except openai.error.APIError as e:
            logger.error(f"OpenAI API error: {e}")
            return "I'm sorry, I encountered an error processing your request."
            
        except Exception as e:
            logger.error(f"Error processing command with AI: {e}")
            return self._fallback_response(command)
    
    def _get_system_prompt(self):
        """Get the system prompt for the AI."""
        return """You are Wakeon, a helpful voice assistant. You should:
1. Provide concise, helpful responses suitable for voice output
2. Keep responses under 100 words when possible
3. Be friendly and conversational
4. Focus on being useful and informative
5. If you don't know something, say so rather than making things up"""
    
    def _fallback_response(self, command):
        """
        Provide fallback responses when OpenAI is not available.
        
        Args:
            command (str): The voice command
            
        Returns:
            str: Fallback response
        """
        command_lower = command.lower()
        
        # Simple keyword-based responses
        if "weather" in command_lower:
            return "I'm sorry, I can't check the weather right now. You might want to look outside or check a weather app."
        
        elif "time" in command_lower:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."
        
        elif "date" in command_lower:
            from datetime import datetime
            current_date = datetime.now().strftime("%B %d, %Y")
            return f"Today is {current_date}."
        
        elif "hello" in command_lower or "hi" in command_lower:
            return "Hello! I'm Wakeon, your voice assistant. How can I help you today?"
        
        elif "help" in command_lower:
            return "I can help you with various tasks. Try asking me about the weather, time, or any general questions. For more advanced features, please configure your OpenAI API key."
        
        elif "joke" in command_lower:
            return "Why don't scientists trust atoms? Because they make up everything!"
        
        elif "name" in command_lower:
            return "My name is Wakeon. I'm your personal voice assistant."
        
        else:
            return "I'm sorry, I'm not sure how to help with that. Try asking me about the weather, time, or for a joke. For more advanced features, please configure your OpenAI API key."
    
    def cleanup(self):
        """Clean up resources."""
        logger.debug("AI processor cleaned up")


class SimpleAIProcessor:
    """Simple AI processor for testing."""
    
    def __init__(self):
        """Initialize simple AI processor."""
        logger.info("Initializing simple AI processor (for testing)")
    
    def process_command(self, command):
        """
        Simulate AI processing.
        
        Args:
            command (str): The voice command
            
        Returns:
            str: Simulated response
        """
        return f"I heard you say: {command}. This is a test response from the simple AI processor."
    
    def cleanup(self):
        """Clean up resources."""
        logger.debug("Simple AI processor cleaned up") 