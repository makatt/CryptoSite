% rebase('layout.tpl', title='�������', year=year)

<div class="container">
    <h1>�������������� �������</h1>
    
    % if error:
        <div class="alert alert-danger">
            {{ error }}
        </div>
    % end
    
    <div class="row">
        <div class="col-md-8">
            <h2>��������� �������</h2>
            
            % if not news_items:
                <p>���� ��� ��������. ������ ������, ��� ������� �������!</p>
            % else:
                % for item in news_items:
                    <div class="news-item card mb-3">
                        <div class="card-body">
                            <h3 class="card-title">{{ item['title'] }}</h3>
                            <div class="card-subtitle mb-2 text-muted">
                                ������������: {{ item['date'] }} | �����: {{ item['author'] }}
                            </div>
                            <p class="card-text">{{ item['content'] }}</p>
                        </div>
                    </div>
                % end
            % end
        </div>
        
        <div class="col-md-4">
            <div class="card">
                <div class="card-header">
                    <h3>�������� �������</h3>
                </div>
                <div class="card-body">
                    <form action="/news" method="post">
                        <div class="form-group">
                            <label for="title">���������</label>
                            <input type="text" class="form-control" id="title" name="title" 
                                value="{{ form_data['title'] if 'form_data' in locals() else '' }}" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="author">�����</label>
                            <input type="text" class="form-control" id="author" name="author"
                                value="{{ form_data['author'] if 'form_data' in locals() else '' }}" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="date">���� ����������</label>
                            <input type="date" class="form-control" id="date" name="date"
                                value="{{ form_data['date'] if 'form_data' in locals() else '' }}" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="content">����������</label>
                            <textarea class="form-control" id="content" name="content" rows="5" required>
                                {{ form_data['content'] if 'form_data' in locals() else '' }}
                            </textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-primary">������������</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .news-item {
        border-left: 4px solid #007bff;
    }
    .news-item:hover {
        box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
    }
</style>