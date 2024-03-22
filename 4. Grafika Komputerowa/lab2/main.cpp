#include<iostream>
#include<glad/glad.h>
#include<GLFW/glfw3.h>

// Vertex Shader source code
const char* vertexShaderSource = "#version 330 core\n"
"layout (location = 0) in vec3 aPos;\n"
"void main()\n"
"{\n"
" gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
"}\0";

//Fragment Shader source code
const char* fragmentShaderSource = "#version 330 core\n"
"out vec4 FragColor;\n"
"void main()\n"
"{\n"
" FragColor = vec4(0.8f, 0.3f, 0.02f, 1.0f);\n"
"}\n\0";

int main() {
	// inicjalizacja glfw
	glfwInit();

	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);

	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	GLFWwindow* window = glfwCreateWindow(800, 800, "Okno OpenGL", NULL, NULL);

	if (window == NULL) {
		std::cout << "Blad tworzenia okna GLFW";
		glfwTerminate();
		return -1;
	}

	glfwMakeContextCurrent(window);
	gladLoadGL();

	// od 0,0 do 800,800
	glViewport(0, 0, 800, 800);

	// specyfikacja koloru t³a
	glClearColor(0.07f, 0.13f, 0.17f, 1.0f);




	// xx
	// xx

	// Utwórz obiekt Vertex Shader
	GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
	// Po³¹cz istniej¹cy obiekt z napisan¹ wczeœniej implementacj¹ shadera
	glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
	// Skompiluj gotowy kod
	glCompileShader(vertexShader);
	// Powtórz operacjê dla fragment shadera
	GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
	glCompileShader(fragmentShader);
	// Utwórz program
	GLuint shaderProgram = glCreateProgram();
	// Pod³¹cz shadery pod program
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	glLinkProgram(shaderProgram);
	// Usuñ niepotrzebne shadery
	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);



	GLfloat vertices[] =
	{
		0.6f, 0.4f, 0.0f, // Lower left corner
		0.6f, -0.6f, 0.0f, // Lower right corner
		-0.4f, -0.6f, 0.0f, // Upper 
	};

	GLfloat triangle2[] =
	{
		0.4f, 0.6f, 0.0f, // Lower left corner
		-0.6f, 0.6f, 0.0f, // Lower right corner
		-0.6f, -0.4f, 0.0f // Upper 
	};



	GLuint VAO[2], VBO[2];
	// Utwórz obiekty VBO i VAO, ka¿dy posiada jeden obiekt
	glGenVertexArrays(2, VAO);
	glGenBuffers(2, VBO);

	// trojkat numer 1
	// Po³¹cz wierzcho³ki z bufforem wierzcho³ków
	glBindVertexArray(VAO[0]);
	// Ustaw typ VBO
	glBindBuffer(GL_ARRAY_BUFFER, VBO[0]);
	// za³aduj przygotowane wierzcho³ki
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
	// Skonfiguruj format buffora, typ danych i d³ugoœæ
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
	// Uruchom buffor
	glEnableVertexAttribArray(0);
	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	// trojkat numer 2
	// Po³¹cz wierzcho³ki z bufforem wierzcho³ków
	glBindVertexArray(VAO[1]);
	// Ustaw typ VBO
	glBindBuffer(GL_ARRAY_BUFFER, VBO[1]);
	// za³aduj przygotowane wierzcho³ki
	glBufferData(GL_ARRAY_BUFFER, sizeof(triangle2), triangle2, GL_STATIC_DRAW);
	// Skonfiguruj format buffora, typ danych i d³ugoœæ
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
	// Uruchom buffor
	glEnableVertexAttribArray(0);
	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);










	while (!glfwWindowShouldClose(window)) {

		// Ustaw kolor t³a (RGBA, z przedzia³u <0, 1>)
		glClearColor(0.07f, 0.13f, 0.17f, 1.0f);
		// Wyczyœæ buffor I nadaj mu kolor
		glClear(GL_COLOR_BUFFER_BIT);
		// Wybierz, który shader bêdzie u¿ywany
		glUseProgram(shaderProgram);


		glBindVertexArray(VAO[0]);
		// Narysuj trójk¹t
		glDrawArrays(GL_TRIANGLES, 0, 3);

		// Ustaw kolor dla 2. trójk¹ta
		glUniform4f(glGetUniformLocation(shaderProgram, "color"), 0.3f, 0.6f, 0.6f, 1.0f);
		glBindVertexArray(VAO[1]);
		// Narysuj trójk¹t
		glDrawArrays(GL_TRIANGLES, 0, 3);

		// Odœwie¿ widok
		glfwSwapBuffers(window);
		glfwPollEvents();

	}
	

	glDeleteVertexArrays(2, VAO);
	glDeleteBuffers(2, VBO);
	glDeleteProgram(shaderProgram);



	glfwDestroyWindow(window);
	// zakoñczenie GLFW
	glfwTerminate();

	return 0;
}