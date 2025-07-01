describe('Primera Automatización en Cypress', function(){
  Cypress.on('uncaught:exception', (err, runnable) => {
  // Ignora todos los errores no controlados
  return false;
});

  beforeEach(() => {
  cy.visit('https://www.pdfdrive.com/');
  cy.screenshot('01.entrar-a-pdfdrive.com');
});

    it('Acceder al sitio web', function(){
      cy.contains('Sign in').click();
      cy.screenshot('02.clicar-signin');    
      cy.wait(1000);
      cy.get('#inputIdentity').type('ivan.camilo.martinez@hotmail.com');
      cy.screenshot('03.input-email');
      cy.wait(1000);
      cy.get('#inputPassword').type('12345678');
      cy.screenshot('04.input-password');
      cy.wait(1000);
      cy.get('button[type="submit"]').contains('Sign in').click();
      cy.screenshot('05.clicar-signin');
      cy.wait(1000);
      cy.get('#q').type('Fotografía');
      cy.screenshot('06.escribir-search-bar');
      cy.wait(1000);
      cy.get('#search-form > button > .fa').click();
      cy.screenshot('07.clicar-icono-search-bar');
      cy.wait(1000);
      cy.get('#save-link-33544282').click();
      cy.screenshot('08.guardar-libro-drive');
      cy.wait(2000);
      cy.get('#download-link-33544282').click();
      cy.screenshot('09.descargar-libro');
      cy.wait(2000);
      cy.get('.dropdown-toggle').click();
      cy.screenshot('10.desplegar-menu');
      cy.wait(2000);
      cy.contains('Logout').click();
      cy.screenshot('11.logout');
      cy.wait(2000);
    })
})