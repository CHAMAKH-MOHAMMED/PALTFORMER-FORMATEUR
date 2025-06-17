from odoo import http
from odoo.http import request

class AcademyTrainersWebsite(http.Controller):

    @http.route('/academy', type='http', auth='public', website=True, sitemap=True)
    def academy_landing_page(self, **kwargs):
        return request.render('academy_trainers_management.academy_landing_page_template')

    @http.route('/trainers', type='http', auth='public', website=True)
    def list_trainers(self, **kwargs):
        # Logic to fetch and display a list of trainers
        # Placeholder: Replace with actual data fetching
        trainers = request.env['academy.trainer.profile'].search([('website_published', '=', True)])
        return request.render('academy_trainers_management.trainers_list_template', {
            'trainers': trainers
        })

    @http.route('/trainers/<model("academy.trainer.profile"):trainer>', type='http', auth='public', website=True)
    def trainer_profile(self, trainer, **kwargs):
        # Logic to display a single trainer's profile
        # Placeholder: Replace with actual data rendering
        if not trainer.website_published and not request.env.user.has_group('academy_trainers_management.group_academy_admin'): # Latter group to be defined
             # Or check if the trainer is the current user if they are logged in
            if not trainer.user_id or trainer.user_id != request.env.user:
                return request.render('website.404') # Or a custom access denied page

        return request.render('academy_trainers_management.trainer_profile_template', {
            'trainer': trainer,
            'page_name': 'trainer_profile', # For template conditional rendering
        })

    @http.route('/trainers/profile/create', type='http', auth='user', website=True, methods=['GET', 'POST'])
    def create_trainer_profile(self, **kwargs):
        # GET: Display form
        # POST: Process form data and create profile
        # This will require a form template and more logic
        # Ensure user is logged in and doesn't already have a profile or has rights
        if request.httprequest.method == 'POST':
            # Process POST data, create trainer profile
            # Ensure proper validation and security
            # Example:
            # vals = {
            # 'name': kwargs.get('name'),
            # 'email': kwargs.get('email'),
            # ... other fields ...
            # 'user_id': request.env.user.id, # Link to current user
            # }
            # new_trainer = request.env['academy.trainer.profile'].sudo().create(vals) # Use sudo carefully
            # return request.redirect(f'/trainers/{new_trainer.id}')
            pass # Placeholder
        return request.render('academy_trainers_management.trainer_profile_form_template', {
            # Pass necessary data to the form, e.g., for selection fields
            'page_name': 'create_trainer_profile',
        })

    @http.route('/trainers/profile/edit', type='http', auth='user', website=True, methods=['GET', 'POST'])
    def edit_trainer_profile(self, **kwargs):
        # GET: Display form for the current user's trainer profile
        # POST: Process form data and update profile
        # This requires logic to find the trainer profile linked to the current user
        trainer = request.env['academy.trainer.profile'].search([('user_id', '=', request.env.user.id)], limit=1)
        if not trainer:
            return request.redirect('/trainers/profile/create') # Or show an error

        if request.httprequest.method == 'POST':
            # Process POST data, update trainer profile
            # trainer.sudo().write(vals) # Use sudo carefully
            pass # Placeholder
        return request.render('academy_trainers_management.trainer_profile_form_template', {
            'trainer': trainer,
            'page_name': 'edit_trainer_profile',
        })

    @http.route('/trainers/profile/cv/upload', type='http', auth='user', website=True, methods=['POST'])
    def upload_trainer_cv(self, **kwargs):
        # Process CV upload
        # This requires a form in the trainer's profile management area
        # Ensure the user is linked to a trainer profile
        trainer = request.env['academy.trainer.profile'].search([('user_id', '=', request.env.user.id)], limit=1)
        if not trainer:
            return request.render('website.403') # Forbidden

        # cv_file = kwargs.get('cv_file')
        # if cv_file:
        # request.env['academy.trainer.cv'].sudo().create({
        # 'name': cv_file.filename,
        # 'cv_file': base64.b64encode(cv_file.read()),
        # 'trainer_id': trainer.id,
        # })
        # return request.redirect('/trainers/profile/edit') # Or back to profile page
        pass # Placeholder
        return request.redirect('/trainers/profile/edit')


    @http.route('/training-centers/profiles', type='http', auth='user', website=True) # Or 'public' depending on requirements
    def list_training_centers(self, **kwargs):
        # Placeholder for listing training centers if needed, or directly to search
        # This might be more of an admin/backend feature or a specific page for centers
        # For now, let's assume centers search trainers
        return request.redirect('/trainers/search') # Redirect to trainer search for now

    @http.route('/trainers/search', type='http', auth='user', website=True, methods=['GET']) # Explicitly GET, form submission is GET
    def search_trainers(self, **kwargs):
        trainers = None # Initialize trainers
        search_domain = [('website_published', '=', True)]

        relevant_search_keys = ['name', 'domain_id', 'availability', 'location']
        # Check if any actual search values are provided for the relevant keys
        has_search_criteria = any(kwargs.get(k) for k in relevant_search_keys)

        if has_search_criteria:
            if kwargs.get('name'):
                search_domain.append(('name', 'ilike', kwargs.get('name')))
            if kwargs.get('domain_id'):
                try:
                    domain_id = int(kwargs.get('domain_id'))
                    if domain_id: # Ensure it's not 0 from an empty select
                         search_domain.append(('domains', 'in', [domain_id]))
                except ValueError:
                    pass # Ignore if domain_id is not a valid integer (e.g. empty string from select)
            if kwargs.get('availability'):
                search_domain.append(('availability', '=', kwargs.get('availability')))
            if kwargs.get('location'):
                search_domain.append(('location', 'ilike', kwargs.get('location')))

            trainers = request.env['academy.trainer.profile'].search(search_domain)
        # If no search criteria effectively provided, trainers remains None (or [] if preferred by template logic)
        # This means if the page is just loaded, no results are shown, which is fine.

        all_domains = request.env['academy.trainer.domain'].search([])

        return request.render('academy_trainers_management.trainers_search_template', {
            'trainers': trainers,
            'search_criteria': kwargs, # Pass kwargs directly, template uses .get() for safety
            'all_domains': all_domains,
            'page_name': 'search_trainers',
            'has_search_criteria': has_search_criteria # For template to show "No results" vs "Enter search criteria"
        })

    # Similar create/edit controllers for TrainingCenterProfile can be added here
    # e.g., /centers/profile/create and /centers/profile/edit
    # These would be auth='user' and link to the user_id on the center profile.
