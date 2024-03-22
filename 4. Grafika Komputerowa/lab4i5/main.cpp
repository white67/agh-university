#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

int main() {
    // Initialize GLFW
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(800, 800, "Openglwindow", NULL, NULL);
    // Error check if the window fails to create
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" <<
            std::endl;
        glfwTerminate();
        return -1;
    }
    // Introduce the window into the current context
    glfwMakeContextCurrent(window);

    //Load GLAD so it configures OpenGL
    gladLoadGL();
    // Specify the viewport of OpenGL in the Window
    // In this case the viewport goes from x = 0, y = 0, to x = 800, y = 800
    glViewport(0, 0, 800, 800);

    // Clean the back buffer and assign the new color to it
    glClear(GL_COLOR_BUFFER_BIT);
    // Swap the back buffer with the front buffer
    glfwSwapBuffers(window);


    // Vertex Shader source code
    const char* vertexShaderSource = "#version 330 core\n"
        "in vec2 position;\n"
        "in vec3 color;\n"
        "out vec3 Color;\n"
        "void main()\n"
        "{\n"
        " Color = color;\n"
        " gl_Position = vec4(position, 0.0, 1.0);\n"
        "}\0";
    //Fragment Shader source code
    const char* fragmentShaderSource = "#version 330 core\n"
        "in vec3 Color;\n"
        "out vec4 outColor;\n"
        "void main()\n"
        "{\n"
        " outColor = vec4(Color, 1.0);\n"
        "}\n\0";


    /*
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
        " FragColor = vec4(0.4f, 0.5f, 0.9f, 1.0f);\n"
        "}\n\0";
    */

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

    // Vertices coordinates

    const int siatka_rozmiar = 7;

    // numVertices = siatka_rozmiar^2 * 3
    const int numVertices = 49 * 3;
    // numIndices = (siatka_rozmiar-1)^2 * 3
    const int numIndices = 36 * 3;

    GLuint indices[numIndices];
    GLfloat vertices[numVertices];

    int index = 0;

    for (int i = 0; i <= siatka_rozmiar-1; i++) {
        float p = (float(i) / float((siatka_rozmiar-1)/2)) - 1.0;

        for (int j = siatka_rozmiar-1; j >= 0; j--) {
            float pp = (float(j) / float((siatka_rozmiar-1)/2)) - 1.0;

            vertices[index++] = p;
            vertices[index++] = pp;
            vertices[index++] = 0.0f;
        }
    }

    index = 0;

    for (int i = 0; i < siatka_rozmiar-1; i++) {
        int p = i + 1;

        for (int j = 0; j < siatka_rozmiar-1; j++) {

            indices[index++] = p + (j) *siatka_rozmiar;
            indices[index++] = p + (j) *siatka_rozmiar + siatka_rozmiar;
            indices[index++] = p + (j) *siatka_rozmiar + siatka_rozmiar-1;
        }
    }


    GLuint VAO, VBO, EBO;
    // Utwórz obiekty VBO i VAO, ka¿dy posiada jeden obiekt
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);
    // Po³¹cz wierzcho³ki z bufforem wierzcho³ków
    glBindVertexArray(VAO);
    // Ustaw typ VBO
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    // za³aduj przygotowane wierzcho³ki
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices,
        GL_STATIC_DRAW);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    // Skonfiguruj format buffora, typ danych i d³ugoœæ
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 *
        sizeof(float), (void*)0);
    // Uruchom buffor
    glEnableVertexAttribArray(0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

    // okreœl uk³ad danych wierzcho³ków
    GLint posAttrib = glGetAttribLocation(shaderProgram, "position");
    glEnableVertexAttribArray(posAttrib);
    /*glVertexAttribPointer(posAttrib, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(float), 0);*/

    // uzyskaj lokalizacjê danych dotycz¹cych koloru wierzcho³ków w programie
    GLint colAttrib = glGetAttribLocation(shaderProgram, "color");
    glEnableVertexAttribArray(colAttrib);
    /*glVertexAttribPointer(colAttrib, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(float), (void*)(2 * sizeof(float)));*/

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(float), (void*)0); // Position
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(float), (void*)(2 * sizeof(float))); // Color




    while (!glfwWindowShouldClose(window))
    {

        // Ustaw kolor t³a (RGBA, z przedzia³u <0, 1>)
        glClearColor(0.1f, 0.2f, 0.3f, 1.0f);

        // Wyczyœæ buffor I nadaj mu kolor
        glClear(GL_COLOR_BUFFER_BIT);
        // Wybierz, który shader bêdzie u¿ywany
        glUseProgram(shaderProgram);


        glBindVertexArray(VAO);
        glDrawElements(GL_TRIANGLES, sizeof(indices) / sizeof(GLuint), GL_UNSIGNED_INT, 0);
        // Odœwie¿ widok
        glfwSwapBuffers(window);
        glfwPollEvents();

    }
    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteBuffers(1, &EBO);

    glDeleteProgram(shaderProgram);

    // Delete window before ending the program
    glfwDestroyWindow(window);
    // Terminate GLFW before ending the program
    glfwTerminate();


    return 0;
}